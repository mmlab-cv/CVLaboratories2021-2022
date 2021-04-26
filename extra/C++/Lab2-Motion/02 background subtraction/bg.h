/*
 * bg.h
 *
 *  Created on: Oct 8, 2018
 *      Author: mmlab
 */

#ifndef BG_H_
#define BG_H_

#include <opencv2/opencv.hpp>

using namespace cv;

void bg_train(Mat frame, Mat* background);
void bg_update(Mat frame, Mat* background);

#endif /* BG_H_ */
