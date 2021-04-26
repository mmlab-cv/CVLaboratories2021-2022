/*
 * main.cpp
 *
 *  Created on: Oct 8, 2018
 *      Author: mmlab
 */


#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>

#include "bg.h"

using namespace cv;

int main(){

	Mat frame, frame_gray;
	Mat bg, motion_mask, motion_thres;

	int nFrames = 1000; //number of frame to process

	VideoCapture cap(0);
	//VideoCapture cap ("Video.mp4");

	if(!cap.isOpened())
		return 0;

	for(int i = 0; i<nFrames; i++){
		cap >> frame;

		if(i>0){
			//color conversion to gray
			cvtColor(frame, frame_gray, COLOR_RGB2GRAY);

			//store first frame as background
			bg_train(frame_gray,&bg);

			//bg subtraction
			absdiff(bg, frame_gray, motion_mask);

			//mask thresholding
			threshold(motion_mask,motion_thres,
					50, 255, THRESH_BINARY);

			//display
			imshow("original", frame);
			imshow("Background", bg);
			imshow("Motion mask", motion_thres);
			waitKey(1);
		}

	}

	return 0;
}

