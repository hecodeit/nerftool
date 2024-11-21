# Readme

## convert.py
Copy from [graphdeco-inria/gaussian-splatting](https://github.com/graphdeco-inria/gaussian-splatting?tab=readme-ov-file#processing-your-own-scenes)

For rasterization, the camera models must be either a SIMPLE_PINHOLE or PINHOLE camera. We provide a converter script convert.py, to extract undistorted images and SfM information from input images. Optionally, you can use ImageMagick to resize the undistorted images. This rescaling is similar to MipNeRF360, i.e., it creates images with 1/2, 1/4 and 1/8 the original resolution in corresponding folders. To use them, please first install a recent version of COLMAP (ideally CUDA-powered) and ImageMagick. Put the images you want to use in a directory <location>/input.
```
<location>
|---images
|   |---<image 0>
|   |---<image 1>
|   |---...
|---sparse
    |---0
        |---cameras.bin
        |---images.bin
        |---points3D.bin
```
If you have COLMAP and ImageMagick on your system path, you can simply run
```
python convert.py -s <location> [--resize] #If not resizing, ImageMagick is not needed
```

## video_to_jpg.py
```
python video_to_jpg.py C:\Users\yulei\Desktop\10-20\DJI_001\DJI_20241020122229_0129_D.MP4 C:\Users\yulei\Desktop\10-20\DJI_001\jpgs\output_%04d.jpg

python video_to_jpg.py /Users/yulei/Desktop/11-09/DJI_20241109120748_0003_D.MP4 /Users/yulei/Desktop/11-09/11-09-three/%04d.jpg
```

## camera_alignment
```
python camera_alignmant.py path/to/the/project/directory

python add_new_images.py /Users/yulei/Desktop/test/wall-d /Users/yulei/Desktop/test/top-b /Users/yulei/Desktop/test/salon-zeus
```