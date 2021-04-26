#include <opencv2/opencv.hpp>

using namespace cv;
using namespace std;

int main()
{

	Mat frame, prev_frame, frame_gray, copy;
    VideoCapture cap;

    int nFrames = 1000;
    int step = 100;
    int maxCorners = 200;

    /// Parameters for Shi-Tomasi algorithm
    vector<Point2f> corners, prev_corners;
    vector<uchar> status;
    vector<float> err;
    double qualityLevel = 0.01;
    double minDistance = 10;
    int blockSize = 3;
    bool useHarrisDetector = false;
    double k = 0.04;

    cap.open(0);
    if(!cap.isOpened())
    	return 0;

    namedWindow("Window",1);

    for(int i = 0; i<nFrames; i++){

    	cap >> frame;

    	copy = frame.clone();

    	cvtColor( frame, frame_gray, COLOR_BGR2GRAY );

    	if ( i % step == 0)
    	{
		//select features to track using GFF
    		goodFeaturesToTrack( frame_gray, corners, maxCorners, qualityLevel, minDistance, Mat(), blockSize, useHarrisDetector, k );

    	}
    	else
    	{
		//tracking
    		calcOpticalFlowPyrLK(prev_frame, frame, prev_corners, corners, status, err);

    	}

        int r = 4;
        for( int j = 0; j < corners.size(); j++ )
           {
        	circle( copy, corners[j], r, Scalar(5*j, 2*j, 255 - j), -1, 8, 0 );
           }

    	prev_frame = frame.clone();
    	prev_corners = corners;

    	imshow("Window", copy);
    	if(waitKey(10) >= 0) break;

    }


    return(0);
}

