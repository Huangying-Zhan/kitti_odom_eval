# KITTI Odometry Evaluation Toolbox
[KITTI Odometry benchmark](http://www.cvlibs.net/datasets/kitti/eval_odometry.php) contains 22 stereo sequences, in which 11 sequences are provided with ground truth. 


The evaluation tool is used for evaluating KITTI odometry result.
We include several common metrics in evaluating visual odometry, including
* sub-sequence translation drift percentage
* sub-sequence rotation error 
* absolute trajectory error
* relative pose error (translation)
* relative pose error (rotation)

## Requirement
We recommend using [Anaconda](https://www.anaconda.com/distribution/) for installing the prerequisites.

```
conda env create -f requirement.yml -p kitti_eval # install prerequisites
conda activate kitti_eval  # activate the environment [kitti_eval]
```

## Result Format
Before evaluation, estimated poses should be saved in a `.txt` file. 
Currently, there are two formats are supported.

Suppose the pose for 100-th image is 
```
T00 T01 T02 T03
T10 T11 T12 T13
T20 T21 T22 T23
0   0   0   1
```
You should save the pose as
```
# First format: skipping frames are allowed
99 T00 T01 T02 T03 T10 T11 T12 T13 T20 T21 T22 T23 

# Second format: all poses should be included in the file
T00 T01 T02 T03 T10 T11 T12 T13 T20 T21 T22 T23
```

## Usage

There are two possible options for using the tool.

### Single evaluation

The basic usage is 
```
# RESULT_PATH:
# - Contains the camera pose text file, 
#    which should be named as 00.txt, 01.txt, ...

# Example
python eval_odom.py --result result/example_1/
```

The full usage is
```
# X:
# - Is the sequence number
# - If not given, all sequences in the folder will be evaluated

python eval_odom.py --result RESULT_PATH --align ALIGNMENT_OPTION --seqs X X X

# Examples
python eval_odom.py --result result/example_0 --align 7dof
python eval_odom.py --result result/example_1 --align 6dof --seqs 9
```

**Note:** The detailed results will be saved in `RESULT_PATH`.


### Multi-prediction evaluation

For multi-prediction evaluation
```
# RESULT_PATH:
# - Is the root path to all method predictions

# PATH_X:
# - Is the relative path of each method inside RESULT_PATH

# X:
# - Is the sequence number

# OUT_PATH:
# - Is the path inside RESULT_PATH where results will be saved

python multi_eval_odom.py --result RESULT_PATH --methods PATH_X PATH_X --seqs X X X --output OUT_PATH
```

**Note:** Multi-prediction also supports the `ALIGNMENT_OPTION`.

## Alignment
Following prior works, certain degrees of alignment can be done in this evaluation script. Pass one of the following arguments `--align XXX` to the script, where `XXX` can be,
* scale
* scale_7dof
* 6dof
* 7dof

### scale
Find a scaling factor that best aligns the predictions to the ground truth (GT) poses

### scale_7dof
Find a 6+1 DoF transformation, including translation, rotation, and scaling, that best align the predictions to the GT poses.
After that, only the scaling factor is used to align the predictions to the GT for evaluation.

### 6dof
Find a 6 DoF transformation, including translation and rotation, that best aligns the predictions to GT poses.

### 7dof
Find a 6+1 DoF transformation, including translation, rotation, and scaling, that best align the predictions to the GT poses.

## Evaluation result
Here are some evaluation result examples
<img src='misc/run_eg.jpeg' width=640 height=160>

Trajectory comparison

<img src='misc/traj_eg.jpeg' width=320 height=320>

Sub-sequence error

<img src='misc/sub_seq_err.jpeg' width=480 height=240>

Result summary

<img src='misc/result_summary.jpeg' width=320 height=240>

## License
The code is released under the permissive MIT license.

If you use this toolbox, a footnote with the link to this toolbox is appreciated.

You can also cite the [DF-VO](https://github.com/Huangying-Zhan/DF-VO) which we release the toolbox in the first place.

```
@article{zhan2019dfvo,
  title={Visual Odometry Revisited: What Should Be Learnt?},
  author={Zhan, Huangying and Weerasekera, Chamara Saroj and Bian, Jiawang and Reid, Ian},
  journal={arXiv preprint arXiv:1909.09803},
  year={2019}
}
```
