import cv2
import numpy as np


# Function to get the full boundary of a binary mask.
def mask_to_boundary_s2fbIoU(mask, dilation_ratio=0.02):
    """
    Convert binary mask to boundary mask.
    :param mask (numpy array, uint8): binary mask
    :param dilation_ratio (float): ratio to calculate dilation = dilation_ratio * image_diagonal
    :return: full band (numpy array)
    """
    h, w = mask.shape
    img_diag = np.sqrt(h ** 2 + w ** 2)
    dilation = int(round(dilation_ratio * img_diag))
    if dilation < 1:
        dilation = 1
    # Pad image so mask truncated by the image border is also considered as boundary.
    new_mask = cv2.copyMakeBorder(mask, 1, 1, 1, 1, cv2.BORDER_CONSTANT, value=0)
    kernel = np.ones((3, 3), dtype=np.uint8)
    new_mask_erode = cv2.erode(new_mask, kernel, iterations=dilation)
    new_mask_dilate = cv2.dilate(new_mask, kernel, iterations=dilation)
    mask_erode = new_mask_erode[1 : h + 1, 1 : w + 1]
    mask_dilate = new_mask_dilate[1 : h + 1, 1 : w + 1]
    
    # get the inner and outer bands
    inner_band = mask - mask_erode
    outer_band = mask_dilate - mask

    # get the full band
    full_band = inner_band + outer_band
    
    return full_band


# Function to get the solidity ratio of a binary mask.
def solidity(mask):
    """
    Compute the solidity ratio of a binary mask.
    :param mask (numpy array, uint8): binary mask
    :return: solidity ratio (float)
    """
    contours, hierarchy = cv2.findContours(mask.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    if not contours:
        return 0
    
    contour_areas = [cv2.contourArea(c) for c in contours]
    largest_contour_idx = np.argmax(contour_areas)
    
    largest_contour = contours[largest_contour_idx]
    convex_hull = cv2.convexHull(largest_contour)
    
    convex_hull_area = cv2.contourArea(convex_hull)
    mask_area = contour_areas[largest_contour_idx]
    
    if convex_hull_area == 0:
        ratio = 1
    else:
        ratio = float(mask_area) / convex_hull_area
    
    return ratio


# Function to get the S2FB IoU score between two binary masks.
def s2fb_iou(gt, dt, dilation_ratio=0.02):
    """
    Compute s2fb iou between two binary masks.
    :param gt (numpy array, uint8): binary mask
    :param dt (numpy array, uint8): binary mask
    :param dilation_ratio (float): ratio to calculate dilation = dilation_ratio * image_diagonal
    :return: boundary iou (float)
    """
    gt_boundary = mask_to_boundary_s2fbIoU(gt, dilation_ratio)
    dt_boundary = mask_to_boundary_s2fbIoU(dt)
    
    intersection = ((gt_boundary * dt_boundary) > 0).sum()
    union = ((gt_boundary + dt_boundary) > 0).sum()
    boundary_iou = (intersection / union)
    
    solidity_gt = solidity(gt)
    solidity_pr = solidity(dt)
    
    return boundary_iou * np.sqrt(solidity_gt * solidity_pr)**((1 - boundary_iou))