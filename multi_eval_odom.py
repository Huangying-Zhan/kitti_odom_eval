import argparse

from kitti_odometry import KittiEvalOdom
import datetime

# Timestamp
now = datetime.datetime.now()
timestamp_str = now.strftime("%Y-%m-%d_%H-%M-%S")

parser = argparse.ArgumentParser(description="KITTI evaluation")
parser.add_argument('--result', type=str, required=True,
                    help="Result directory")
parser.add_argument(
    "--methods",
    type=str,
    required=True,
    nargs="+",
    help="Methods directories",
)
parser.add_argument(
    "--align",
    type=str,
    choices=["scale", "scale_7dof", "7dof", "6dof"],
    default=None,
    help="alignment type",
)
parser.add_argument(
    "--seqs", nargs="+", type=int, help="sequences to be evaluated", default=None
)
parser.add_argument(
    "--output", type=str, help="Output directory", default=f"multi_eval_{timestamp_str}/"
)
args = parser.parse_args()

eval_tool = KittiEvalOdom()
gt_dir = "dataset/kitti_odom/gt_poses"
result_dir = args.result

continue_flag = input("Evaluate result in {}? [y/n]".format(result_dir))
if continue_flag == "y":
    eval_tool.multi_eval(
        gt_dir,
        result_dir,
        output_dir=args.output,
        methods=args.methods,
        alignment=args.align,
        seqs=args.seqs,
    )
else:
    print("Double check the path!")
