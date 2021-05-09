import copy
import numpy as np
import open3d as o3d

def rknn_test(pcd):
	r"""
	Method which tests the functionality of the Hybrid KDTree build for finding nearest neighbours 
	with open3d. The Hybrid KNN combines the the KNN search with the RNN search returning at most k 
	nearest neighbors that have distances to the anchor point less than a given radius.

	:param pcd: input point cloud
	"""
	print("Paint the point cloud gray.")
	pcd.paint_uniform_color([0.5, 0.5, 0.5])
	pcd_tree = o3d.geometry.KDTreeFlann(pcd)

	print("Paint the 1st point red.")
	pcd.colors[1] = [1, 0, 0]

	print("Find its 2000 nearest neighbors and paint them blue.")
	[k, idx, _] = pcd_tree.search_knn_vector_3d(pcd.points[1500], 2000)
	np.asarray(pcd.colors)[idx[1:], :] = [0, 0, 1]

	print("Find its neighbors with distance less than 0.02 and paint them green.")
	[k, idx, _] = pcd_tree.search_radius_vector_3d(pcd.points[1500], 0.02)
	np.asarray(pcd.colors)[idx[1:], :] = [0, 1, 0]

	print("Visualize the point cloud.")
	o3d.visualization.draw_geometries([pcd])


def display_outlier(cloud, ind):
	r"""
	Helper which graphically visualise inlier and outliers.

	:param cloud: input point cloud 
	:param ind: inlier indices
	"""

	inlier = cloud.select_by_index(ind)
	outlier = cloud.select_by_index(ind, invert=True)

	print("Showing outliers (red) and inliers (gray): ")
	outlier.paint_uniform_color([1, 0, 0])
	inlier.paint_uniform_color([0.8, 0.8, 0.8])
	o3d.visualization.draw_geometries([inlier, outlier])


if __name__ == "__main__":
	# Creates the reference frame with the axis
	ref_frame = o3d.geometry.TriangleMesh.create_coordinate_frame(size=0.025, origin=[0,0,0])
	o3d.visualization.draw_geometries([ref_frame])
