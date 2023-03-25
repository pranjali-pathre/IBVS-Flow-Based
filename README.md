install habitat and habitat-sim as per the github directions.

get nvidia-flownet2-pytorch repo in flownet folder @ 2e9e010
and run ./install.sh there

To run:
* `git clone https://github.com/pranjali-pathre/IBVS-Flow-Based/`
* `cd IBVS-Flow-Based`
* `scp -r pranjali@10.1.98.140:/home/pranjali/Documents/VisualServoing/FlowNet2_checkpoint.pth.tar ./data/`
* `git clone https://github.com/pranjali-pathre/deepMPCVS`
* `mv deepMPCVS flownet`
* `conda activate deepmpcvs`
* scp pranjali@10.1.98.140:/home/pranjali/Documents/VisualServoing/data_dfvs/data/skokloster-castle/des.png ./
* `python run_dfvs.py ./data/skokloster-castle`
* `./make_video.sh ./data/skokloster-castle && ./plot.py`
