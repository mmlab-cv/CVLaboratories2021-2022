/*
 * bg.cpp
 *
 *  Created on: Oct 8, 2018
 *      Author: mmlab
 */

#include "bg.h"

static int ctr = 1;

void bg_train(Mat frame, Mat* background){
	if(ctr == 1){
		printf("initial background storage..\n");
		frame.copyTo(*background);
	}

	ctr ++;
}


void bg_update(Mat frame, Mat* background){

}

