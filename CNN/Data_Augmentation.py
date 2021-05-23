# -*- coding: utf-8 -*-
"""
Created on Fri May  1 12:13:31 2020

@author: xiali
"""
import os
import numpy as np
from PIL import Image
from pylab import *
from scipy import ndimage, misc
import matplotlib
import matplotlib.pyplot as plt

params = {
    'path_image': ".\images",
    'path_label': ".\labels",
    'path_augmen_image': ".\images_augmentation",
    'path_augmen_label': ".\labels_augmentation",
    'norm_image': 255.,
    'norm_label': 1.,
    'crop_size_x': 224,
    'crop_size_y': 224,
    'aug_flip': ['0', 'lr', 'ud'],
    'aug_rotate': [-60, -50, -40, -30, -20, -10, 10, 20, 30, 40, 50, 60],
    }



def crop_center(img, cropx, cropy):
    y, x = img.shape
    startx = x//2 - (cropx//2)
    starty = y//2 - (cropy//2)    
    return img[starty:starty+cropy,startx:startx+cropx]



def run_data_augmentation(params):        
    name_image =  os.listdir(params['path_image'])
    name_label =  os.listdir(params['path_label'])
    assert(len(name_image)==len(name_label))
    
    for ni in range(len(name_image)):    
        I_img = np.array(Image.open(os.path.join(params["path_image"], name_image[ni]))).mean(axis=-1)
        I_lbl = np.array(Image.open(os.path.join(params["path_label"], name_label[ni])))
        img_name = name_image[ni].split(".")[0]
        lbl_name = name_label[ni].split(".")[0]
        
        for nflip in params["aug_flip"]:
            if nflip == '0':
                I_img_flip = I_img
                I_lbl_flip = I_lbl
            elif nflip == 'lr':
                I_img_flip = np.fliplr(I_img)
                I_lbl_flip = np.fliplr(I_lbl)
            elif nflip == 'ud':
                I_img_flip = np.flipud(I_img)
                I_lbl_flip = np.flipud(I_lbl)
            else:
                raise SyntaxError(f"Data flip augmentation type should be chosen from ['0', 'lr', 'ud'].")            
                
            for nrotate in params['aug_rotate']:
                I_img_flip_rotate = ndimage.rotate(I_img_flip, nrotate, reshape=True, mode='wrap')
                I_lbl_flip_rotate = ndimage.rotate(I_lbl_flip, nrotate, reshape=True, mode='wrap')
        
                I_img_aug = crop_center(I_img_flip_rotate, params['crop_size_x'], params['crop_size_x'])
                I_lbl_aug = crop_center(I_lbl_flip_rotate, params['crop_size_x'], params['crop_size_x'])
            
                img_save_name = f"{img_name}_flip{nflip}_rot{nrotate}.png"
                lbl_save_name = f"{lbl_name}_flip{nflip}_rot{nrotate}.png"
                
                # img_save = Image.fromarray(I_img_aug)
                # lbl_save = Image.fromarray(I_lbl_aug)
                # img_save.save(os.path.join(params['path_augmen_image'], img_save_name))
                # lbl_save.save(os.path.join(params['path_augmen_label'], lbl_save_name))
                
                matplotlib.image.imsave(os.path.join(params['path_augmen_image'], img_save_name), I_img_aug)
                matplotlib.image.imsave(os.path.join(params['path_augmen_label'], lbl_save_name), I_lbl_aug)
                
                print(f"Augmentation of {name_image[ni]} was finished.")
                print(f"Augmentation of {name_label[ni]} was finished.")
                print('... ...')

        
        
    
if __name__ == '__main__':
    
    run_data_augmentation(params)      
        
        