import subprocess, os

def convert_to_hls_async(input_video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    base_name = os.path.splitext(os.path.basename(input_video_path))[0]
    m3u8_path = os.path.join(output_dir, f"{base_name}.m3u8")

    command = [
        'ffmpeg', '-i', input_video_path,
        '-profile:v', 'baseline', '-level', '3.0',
        '-start_number', '0', '-hls_time', '10',
        '-hls_list_size', '0', '-f', 'hls', m3u8_path
    ]
    subprocess.Popen(command)  
    return m3u8_path
