import cv2, pygame as pg

def display_overlay(i, frame):

    overlay = cv2.imread(f"emoji/emoji{i}.png")

    scale = 0.47

    h, w = overlay.shape[0:2]

    overlay = cv2.resize(overlay, (int(w*scale), int(h*scale)))

    h, w = overlay.shape[0:2]

    x, y = 300, 350

    frame[y:y+h, x:x+w] = overlay

    return frame

def phonk(j):
    wav = pg.mixer.Sound(f"phonk/phonk{j}.wav")
    wav.play()


def smilescore(lms):

    left_corner=61
    right_corner=291
    chin=152
    forehead=10
    upper_lip=13

    avgycorner = (lms[left_corner].y + lms[right_corner].y)/2
    faceheight = abs(lms[chin].y - lms[forehead].y)

    lift = lms[upper_lip].y - avgycorner

    normalizedlift = lift/faceheight

    return normalizedlift