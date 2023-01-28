# number_captcha_solver_opencv

This script try to solve numerical captcha as such as,

![Alt text](captchas/captcha_0.png?raw=true "captcha_0")

I have done simple image processing to get only letters from the image with help of
opencv and easyocr.

# HowTo use the script

1. Clone the script
2. Install requirements.txt
3. if your captcha are different than mine, then run the find_param script and
   detect required info into mask image and save that param values (hue, saturation and value)
4. use found param values in main.py file

# References

1. https://github.com/computervisiondeveloper/color-detection-opencv
2. https://github.com/computervisiondeveloper/text-detection-python-easyocr