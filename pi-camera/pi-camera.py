#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# ============================================================================
# PiCamera - Rudimentary Raspberry Pi camera control script
# Copyright (C) 2017 by Ralf Kilian
# Distributed under the MIT License (https://opensource.org/licenses/MIT)
#
# GitHub: https://github.com/urbanware-org/raspberry-pi
# GitLab: https://gitlab.com/urbanware-org/raspberry-pi
# ============================================================================

import picamera
import sys
import time

pr_x = 1024
pr_y = 768
zoom = 0.0

cam = picamera.PiCamera()
cam.resolution = str(pr_x) + "x" + str(pr_y)
cam.image_denoise = True
cam.sharpness = 100
cam.rotation = 180


def rotate_camera(clockwise=True):
    if clockwise:
        cam.rotation += 90
    else:
        cam.rotation -= 90

    if cam.rotation < 0 or cam.rotation > 270:
        cam.rotation = 0


def goodbye():
    cam.close()
    print
    print "Goodbye!"
    print
    sys.exit()


def setup_menu():
    print


def main_menu():
    global zoom
    print
    print "=================================================================="
    print "Main menu"
    print "=================================================================="
    print
    print "Camera settings:"
    print
    print "  - Image resolution:        " + str(cam.resolution)
    print "  - Preview resolution:      " + str(pr_x) + "x" + str(pr_y)
    print "  - Capture resolution:      " + str(cam.MAX_RESOLUTION)
    print "  - Image denoise:           " + str(cam.image_denoise)
    print "  - Sharpness:               " + str(cam.sharpness)
    print "  - Rotation (clockwise):    " + str(cam.rotation)
    print "  - Zoom level:              " + str(zoom)
    print
    print "Please make a choice:"
    print
    print "  1 - Enable preview (adjust camera)"
    print "  2 - Disable preview"
    print "  3 - Capture image"
    print "  4 - Rotate clockwise"
    print "  5 - Rotate counter-clockwise"
    print "  6 - Zoom in"
    print "  7 - Zoom out"
    print
    print "  0 - Exit"
    print
    choice = raw_input("> ")
    if len(choice) > 0:
        try:
            choice = int(choice)
        except:
            print
            print "Invalid input"
            main_menu()

        # Handle the given choice
        if choice == 0:
            goodbye()
        elif choice == 1:
            cam.start_preview(fullscreen=False, window=(800, 228, pr_x, pr_y))
        elif choice == 2:
            cam.stop_preview()
        elif choice == 3:
            cam.capture("capture_sample.jpg")
        elif choice == 4:
            rotate_camera(True)
        elif choice == 5:
            rotate_camera(False)
        elif choice == 6:
            zoom += float(0.1)
            if zoom > 0.9:
                zoom = 1.0
            cam.zoom = (zoom, zoom, 1.0, 1.0)
        elif choice == 7:
            zoom -= float(0.1)
            if zoom < 0.1:
                zoom = 0.0
            cam.zoom = (zoom, zoom, 1.0, 1.0)
        else:
            print
            print "Invalid choice"
    main_menu()


def capture(filename, delay=0):
    cam.capture(filename)
    time.sleep(delay)


main_menu()

# EOF
