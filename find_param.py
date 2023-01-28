import cv2

"""
This script is help to find color range for target object. 
In this case, we can try to manipulate Trackbar until we can see only Numbers without any noise or color
"""


def empty(a):
    pass


def find_param(captcha: str = 'captchas/captcha_0.png'):
    captcha_img = cv2.imread(captcha)

    # Convert imaget into HSV space
    img_hsv = cv2.cvtColor(captcha_img, cv2.COLOR_BGR2HSV)

    # in Real world image color does not have same value, because of shadows and noise
    # hence we have to use range of colors
    h_min = 0  # 0
    s_min = 0  # 0
    v_min = 0  # 101

    h_max = 255  # 179
    s_max = 255  # 255
    v_max = 255  # 255

    # A window with 'Display' name is created
    # with WINDOW_AUTOSIZE, window size is set automatically
    cv2.namedWindow("Parameters", cv2.WINDOW_AUTOSIZE)
    cv2.createTrackbar("Hue Min", "Parameters", 0, 179, empty)
    cv2.createTrackbar("Hue Max", "Parameters", 179, 179, empty)
    cv2.createTrackbar("Sat Min", "Parameters", 0, 255, empty)
    cv2.createTrackbar("Sat Max", "Parameters", 255, 255, empty)
    cv2.createTrackbar("Val Min", "Parameters", 0, 255, empty)
    cv2.createTrackbar("Val Max", "Parameters", 255, 255, empty)

    while True:
        h_min = cv2.getTrackbarPos("Hue Min", "Parameters")
        h_max = cv2.getTrackbarPos("Hue Max", "Parameters")
        s_min = cv2.getTrackbarPos("Sat Min", "Parameters")
        s_max = cv2.getTrackbarPos("Sat Max", "Parameters")
        v_min = cv2.getTrackbarPos("Val Min", "Parameters")
        v_max = cv2.getTrackbarPos("Val Max", "Parameters")

        lower_limits = (h_min, s_min, v_min)
        upper_limits = (h_max, s_max, v_max)
        mask = cv2.inRange(img_hsv, lower_limits, upper_limits)

        cv2.imshow('captcha', captcha_img)
        cv2.imshow("img_hsv", img_hsv)
        cv2.imshow("mask", mask)

        # Waiting 0ms for user to press any key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Using cv2.destroyAllWindows() to destroy
    # all created windows open on screen
    cv2.destroyAllWindows()


if __name__ == "__main__":
    find_param()
