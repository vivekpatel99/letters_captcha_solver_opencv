import cv2
import easyocr


def main(captcha: str = 'captchas/captcha_1.png'):
    captcha_img = cv2.imread(captcha)

    scale = 4
    width = int(captcha_img.shape[1] * scale)
    height = int(captcha_img.shape[0] * scale)
    dim = (width, height)

    captcha_img = cv2.resize(captcha_img, dim, interpolation=cv2.INTER_AREA)
    # Convert image into HSV space
    img_hsv = cv2.cvtColor(captcha_img, cv2.COLOR_BGR2HSV)

    # these value can be found with help of find_param script
    h_min = 0
    s_min = 0
    v_min = 101

    h_max = 179
    s_max = 255
    v_max = 255

    lower_limits = (h_min, s_min, v_min)
    upper_limits = (h_max, s_max, v_max)

    mask = cv2.inRange(img_hsv, lower_limits, upper_limits)

    # instance text detector
    reader = easyocr.Reader(['en'], gpu=False)
    # detect text on image
    text_ = reader.readtext(mask)
    threshold = 0.25
    for t_, t in enumerate(text_):
        print(text_)

        bbox, text, score = t
        print(bbox)
        if score > threshold:
            cv2.rectangle(captcha_img, bbox[0], bbox[2], (255, 0, 255), 2)
            cv2.putText(captcha_img, text, bbox[0], cv2.FONT_HERSHEY_COMPLEX, 0.70, (255, 0, 255), 2)

    cv2.imshow('captcha', captcha_img)
    cv2.imshow("img_hsv", img_hsv)
    cv2.imshow("mask", mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
