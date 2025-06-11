import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

def kenar_tespiti(gray):
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    gray_eq = clahe.apply(gray)
    blurred = cv2.GaussianBlur(gray_eq, (3, 3), 0.5)
    edges = cv2.Canny(blurred, 170, 270)
    return edges

def hough_transform(edges, min_radius, max_radius, step=2, threshold=0.6):
    height, width = edges.shape
    edge_points = np.argwhere(edges > 0) 
    accumulator = {}
    for y, x in edge_points:
        for r in range(min_radius, max_radius+1, step):
            for t in range(0, 360, 4):
                a = int(x - r * np.cos(np.deg2rad(t)))
                b = int(y - r * np.sin(np.deg2rad(t)))
                if 0 <= a < width and 0 <= b < height:
                    key = (a, b, r)
                    accumulator[key] = accumulator.get(key, 0) + 1
    if not accumulator:
        return []
    max_vote = max(accumulator.values())
    vote_threshold = int(max_vote * threshold)
    circles = []
    for (a, b, r), v in accumulator.items():
        if v > vote_threshold:
            circles.append((a, b, r, v))
    return circles

def nms_circles(circles, min_dist=40, min_radius_diff=8, max_circles=3):
    filtered = []
    # Büyük yarıçapı ve oyu öne al
    for (a, b, r, v) in sorted(circles, key=lambda x: (-x[2], -x[3])):
        too_close = False
        for (fa, fb, fr, fv) in filtered:
            if np.hypot(a-fa, b-fb) < min_dist:
                too_close = True
                break
        if not too_close:
            filtered.append((a, b, r, v))
        if len(filtered) == max_circles:
            break
    return filtered

def para_siniflandirma(r):
    if 85 <= r <= 88:
        return "5 TL", 5.00
    elif 78 <= r < 85:
        return "1 TL", 1.00
    elif 68 <= r < 78:
        return "50 Kurus", 0.50
    else:
        return "Bilinmeyen", 0.00

def main():
    img = cv2.imread("paralar.jpg")
    if img is None:
        print("Resim bulunamadı!")
        return
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    start = time.time()

    edges = kenar_tespiti(gray)
    circles = hough_transform(edges, min_radius=68, max_radius=88, step=1, threshold=0.45)
    circles = nms_circles(circles, min_dist=40, min_radius_diff=8, max_circles=3)
    end = time.time()
    print(f"İşlem süresi: {end - start:.2f} saniye")
    output = img.copy()
    toplam = 0
    for i, (a, b, r, v) in enumerate(circles):
        label, val = para_siniflandirma(r)
        toplam += val
        cv2.circle(output, (a, b), r-4, (0,255,0), 2)
        cv2.circle(output, (a, b), 2, (0,0,255), 3)
        cv2.putText(output, f"{label} ({val:.2f} TL)", (a-40, b-r-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,0), 2, cv2.LINE_AA)
        print(f"Para {i+1}: {label}")
    print(f"Toplam: {toplam:.2f} TL")
    plt.figure(figsize=(8,8))
    plt.title("Tespit Edilen Paralar")
    plt.imshow(cv2.cvtColor(output, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    main()