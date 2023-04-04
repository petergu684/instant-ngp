source ~/anaconda3/etc/profile.d/conda.sh
conda activate pixsfm
for i in $(seq -f "%03g" 0 0)
do
export WS_PATH=/mnt/hdd1/slam_data/CadaverImages/WithPin/scene1_split_150/scene1_$i
colmap model_converter --input_path $WS_PATH \
    --output_path $WS_PATH \
    --output_type TXT
python /home/wenhao/Documents/instant-ngp/scripts/colmap2nerf.py --images $WS_PATH/images \
    --text $WS_PATH \
    --out $WS_PATH/transforms.json
done
conda deactivate