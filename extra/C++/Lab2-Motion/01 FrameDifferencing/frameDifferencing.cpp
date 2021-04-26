#include <stdio.h>
#include <stdlib.h>

#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;

int main() {

	int nf = 15; //temporal extension for the 3 frame diff..

	Mat myPicture, myPicture_gray, bg;
	Mat D1, b1, motion_mask;

	Mat* Pic = new Mat[1000];

	int nFrames = 1000;
	//VideoCapture cap("Video.mp4");
	VideoCapture cap(0);

	if (!cap.isOpened())
		return 0;

	for (int i = 0; i < nFrames; i++) {
		cap >> myPicture;

		cvtColor(myPicture, myPicture_gray, COLOR_RGB2GRAY);

		myPicture_gray.copyTo(Pic[i]);

		if (i > nf) //need at least 3 frame (for 3-frame difference)
		{

			absdiff(Pic[i], Pic[i-nf], D1);

			//mask thresholding
			threshold(D1, b1, 50, 255, THRESH_BINARY);

			motion_mask = b1;

			//results display
			imshow("Motion", motion_mask);
			imshow("Original", Pic[i]);
			waitKey(30);
		}

	}

	delete[] Pic;
	return 0;

}