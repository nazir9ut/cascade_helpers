import cv2

def adjust_window(img, win_name = 'img'):



    if(img.shape[0] > 1200):
        print("HEIGHT TOO LARGE")
        aspect = 1200.0 / img.shape[0]
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(win_name, int(img.shape[1] * aspect), 1200)
        print(int(img.shape[1] * aspect))
    elif(img.shape[1] > 1920):
        print("WIDTH TOO LARGE")
        aspect = 1920.0 / img.shape[1]
        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(win_name, 1920, int(img.shape[0] * aspect))
    else:
        print("NO RESIZE")
        cv2.namedWindow(win_name)
