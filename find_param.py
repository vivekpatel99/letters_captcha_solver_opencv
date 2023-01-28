import cv2


def empty(a):
    pass


def find_param(captcha: str = 'captchas/captcha_0.png'):
    captcha_img = cv2.imread(captcha)

    # Convert imaget into HSV space
    img_hsv = cv2.cvtColor(captcha_img, cv2.COLOR_BGR2HSV)

    # in Real world image color does not have same value, because of shadows and noise
    # hence we have to use range of colors
    hmin = 0
    smin = 0
    vmin = 128

    hmax = 255
    smax = 255
    vmax = 255

    # A window with 'Display' name is created
    # with WINDOW_AUTOSIZE, window size is set automatically
    cv2.namedWindow("Parameters", cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("hue", "Parameters", 179, 255, empty)
    cv2.createTrackbar("sat", "Parameters", 179, 255, empty)
    cv2.createTrackbar("val", "Parameters", 179, 255, empty)

    while True:
        hue = cv2.getTrackbarPos("hue", "Parameters")
        sat = cv2.getTrackbarPos("sat", "Parameters")
        val = cv2.getTrackbarPos("val", "Parameters")

        img_canny = cv2.Canny(img_hsv, )
        cv2.imshow("Image", img)
        cv2.imshow("imgHSV", img_hsv)
        cv2.imshow("mask", mask)
        cv2.imshow('captcha', captcha_img)

        # Waiting 0ms for user to press any key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Using cv2.destroyAllWindows() to destroy
    # all created windows open on screen
    cv2.destroyAllWindows()


if __name__ == "__main__":
    find_param()
