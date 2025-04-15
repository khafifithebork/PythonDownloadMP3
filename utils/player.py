import pygame

def play_audio(file_path):
    """
    Plays an audio file.
    Args:
        file_path (str): Path to the audio file to play.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    print("Playing audio... Press CTRL+C to stop.")
    try:
        while pygame.mixer.music.get_busy():
            pass  # Wait for playback to finish
    except KeyboardInterrupt:
        print("Stopping playback...")
        pygame.mixer.music.stop()

