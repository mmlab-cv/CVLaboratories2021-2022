#include <iostream>
#include <vector>

#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;


struct mouse_info_struct { int x,y; };
struct mouse_info_struct mouse_info = {-1,-1}, last_mouse;

vector<Point> mousev,kalmanv;

void on_mouse(int event, int x, int y, int flags, void* param) {
	{
		last_mouse = mouse_info;
		mouse_info.x = x;
		mouse_info.y = y;

	}
}

// plot points
#define drawCross( center, color, d )                                 \
line( img, Point( center.x - d, center.y - d ),                \
Point( center.x + d, center.y + d ), color, 2, CV_8U, 0); \
line( img, Point( center.x + d, center.y - d ),                \
Point( center.x - d, center.y + d ), color, 2, CV_8U, 0 )

int main () {
    Mat img(1000, 1000, CV_8UC3);

    //Dynamic parameters(4/6) and measurement parameters (2)
    //KalmanFilter KF(6, 2, 0);
    KalmanFilter KF(4, 2, 0);
    //Mat_<float> state(6, 1); /* (x, y, Vx, Vy, Ax, Ay) */
    Mat_<float> state(4, 1); /* (x, y, Vx, Vy) */
    //Mat processNoise(6, 1, CV_32F);
    Mat processNoise(4, 1, CV_32F);
    //save measurements
    Mat_<float> measurement(2,1); measurement.setTo(Scalar(0));

	namedWindow("mouse kalman");
	setMouseCallback("mouse kalman", on_mouse, 0);

    KF.statePre.at<float>(0) = mouse_info.x;
	KF.statePre.at<float>(1) = mouse_info.y;
	KF.statePre.at<float>(2) = 0;
	KF.statePre.at<float>(3) = 0;
	//KF.statePre.at<float>(4) = 0;
	//KF.statePre.at<float>(5) = 0;
	//KF.transitionMatrix = *(Mat_<float>(6, 6) << 1,0,1,0,0.5,0,   0,1,0,1,0,0.5,  0,0,1,0,1,0,  0,0,0,1,0,1,    0,0,0,0,1,0,    0,0,0,0,0,1 );
	KF.transitionMatrix = (Mat_<float>(4, 4) << 1,0,1,0,   0,1,0,1,  0,0,1,0,  0,0,0,1);

	setIdentity(KF.measurementMatrix);
    setIdentity(KF.processNoiseCov, Scalar::all(1e-4));
    setIdentity(KF.measurementNoiseCov, Scalar::all(0.1));
    setIdentity(KF.errorCovPost, Scalar::all(.1));

    mousev.clear();
    kalmanv.clear();

    for(;;)
    {
      	//Predict, to update the internal statePre variable
        Mat prediction = KF.predict();
        Point predictPt(prediction.at<float>(0),prediction.at<float>(1));

        //Measurement
        measurement(0) = mouse_info.x;
		measurement(1) = mouse_info.y;

		Point measPt(measurement(0),measurement(1));
		mousev.push_back(measPt);

		//Update phase
		Mat estimated = KF.correct(measurement);
		Point statePt(estimated.at<float>(0),estimated.at<float>(1));
		kalmanv.push_back(statePt);

        img = Scalar::all(0);
        drawCross( statePt, Scalar(255,255,255), 5 );
        drawCross( measPt, Scalar(0,0,255), 5 );
        drawCross( predictPt, Scalar(0,255,0), 5 );

		for (int i = 0; i < mousev.size()-1; i++) {
			line(img, mousev[i], mousev[i+1], Scalar(255,255,0), 1);
		}
		for (int i = 0; i < kalmanv.size()-1; i++) {
			line(img, kalmanv[i], kalmanv[i+1], Scalar(0,255,0), 1);
		}

        imshow( "mouse kalman", img );
        waitKey(100);

    }

    return 0;
}