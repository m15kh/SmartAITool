import cv2
import os
import tqdm
import re

def get_video_info(video_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    cap.release()
    return {"fps": fps, "width": width, "height": height, "total_frames": total_frames}


def extract_frames(input_video_path, output_video_dir, start_frame=None, end_frame=None, show_log=True):
    if not os.path.exists(output_video_dir):
        os.makedirs(output_video_dir)
    
    # Get video properties
    fps, width, height, total_frames = get_video_info(input_video_path).values()
    print(f'Video FPS: {fps}, Width: {width}, Height: {height}, Total frames: {total_frames}')
    
    if start_frame is None:
        start_frame = 0
    if end_frame is None:
        end_frame = total_frames
        
    assert start_frame < end_frame, "Start frame must be less than end frame"
    assert end_frame <= total_frames, "End frame must be less than or equal to total frames"
    
    cap = cv2.VideoCapture(input_video_path)
    
    frame_count = 0
    with tqdm(total=(end_frame - start_frame), desc="Extracting frames") as pbar:
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if frame_count >= start_frame and frame_count < end_frame:
                output_video_path = os.path.join(output_video_dir, f'frame_{frame_count}.jpg')
                cv2.imwrite(output_video_path, frame)
                if show_log:
                    print(f"Frame {frame_count} saved to {output_video_path}")
                    frame_count += 1
            pbar.update(1)
    cap.release()
    print(f"Frames saved to {output_video_dir}")


def create_video(input_frames_dir, output_video_path, fps=30):
    frames = []
    for frame_name in sorted_nicely(os.listdir(input_frames_dir)):
        frame_path = os.path.join(input_frames_dir, frame_name)
        frame = cv2.imread(frame_path)
        frames.append(frame)
    
    height, width, _ = frames[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    for frame in tqdm(frames, desc='Creating Video'):
        out.write(frame)
    
    out.release()
    print(f"Video saved to {output_video_path}")
    
    
def sorted_nicely(l):
    """ Sort the given iterable in the way that humans expect."""
    convert = lambda text: int(text) if text.isdigit() else text
    alphanum_key = lambda key: [convert(c) for c in re.split('([0-9]+)', key)]
    return sorted(l, key=alphanum_key)

