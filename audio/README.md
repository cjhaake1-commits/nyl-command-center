# Florida 2-15 Audio Study Guides

The Streamlit Exam Training Center exposes three audio study-guide slots:

1. `florida_215_audio_study_guide.mp3` — rapid review.
2. `florida_215_in_depth_audio_guide.mp3` — longer comprehensive review.
3. `florida_215_exam_day_30min.mp3` — approximately 30-minute exam-day drive review.

Audio files should be placed in this `audio/` directory before deployment. The app checks for each file and renders a Streamlit audio player when present.

The narration scripts are stored alongside the app as text so they can be regenerated with the preferred TTS provider without changing study content. Do not use recalled/live exam questions in any recording.