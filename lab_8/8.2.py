import cv2


lower_black = 0
upper_black = 50
cap = cv2.VideoCapture(0)
img = cv2.imread("fly64.png")


print("Press q to exit")
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, upper_black, 255, cv2.THRESH_BINARY_INV)
    thresh = cv2.medianBlur(thresh, 3)

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    candidate_contours = []
    for contour in contours:
        # Прямоугольник
        x, y, w, h = cv2.boundingRect(contour)

        # Проверка на секторы
        sector1 = thresh[y+h//4:y+h//2, x+w//4:x+w//2]
        sector2 = thresh[y+h//2:y+3*h//4, x+w//2:x+3*w//4]
        if cv2.countNonZero(sector1) > sector1.size * 0.3 and cv2.countNonZero(sector2) > sector2.size * 0.3:
            # if cv2.minEnclosingCircle(contour)[1] <= 150:
            candidate_contours.append(contour)

    # Контур
    if candidate_contours:
        largest_contour = max(candidate_contours, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(largest_contour)

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 0), 2)
            cv2.putText(frame, f"({int(x)}, {int(y)})", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Муха
            try:
                x1, x2 = int(x - 32), int(x + 32)
                y1, y2 = int(y - 32), int(y + 32)
                frame[y1:y2, x1:x2] = img
            except:
                pass

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
