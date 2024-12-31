from utils.video_utils import read_video, save_video, detect_vehicles
from object_tracker.tracker_2 import Tracker

# def main():

#     frames = read_video("data/demo.mp4")

#     #object tracking
#     obj_tracker = Tracker()
#     result = obj_tracker.detect_objects(frames)

#     output_frames = obj_tracker.draw_annotations(frames, result)

#     save_video(output_frames, "output/demo8output4.avi")

###### Main function for 1 image

# def main():
#
#     frames = read_video("data/image.jpg")
#
#     #object tracking
#     obj_tracker = Tracker()
#     result = obj_tracker.detect_frame(frames)
#     print(result)
#
#     # output_frames = obj_tracker.draw_annotations(frames, result)
#     #
#     #
#     # save_video(output_frames, "output/output.avi")


# from object_tracker.tracker_2 import Tracker

# def main():
#
#     frames = read_video("data/traffic_video.mp4")
#
#     #object tracking
#     obj_tracker = Tracker()
#     result = obj_tracker.detect_objects(frames)
#     output_frames = obj_tracker.draw_annotations(frames, result)
#
#
#     output_frames = obj_tracker.process_video(frames)
#
#
#     # save_video(output_frames, "output/123.avi")


from object_tracker.tracker_3 import Tracker
def main():
    frames = read_video("data/traffic_video.mp4")

    track = Tracker()
    result = track.process_video(frames)

if __name__ == '__main__':
    main()


