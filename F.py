import cv2

class FaceOverlay:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        self.cascade = cv2.CascadeClassifier('face.xml')
        self.specs_ori = cv2.imread("glass.png", -1)
        self.cigar_ori = cv2.imread("cigar.png", -1)
        self.mus_ori = cv2.imread("mustache.png", -1)

    def transparent_overlay(self, src, overlay, pos=(0, 0), scale=1):
        # ... (same as before)

    def process_frame(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.cascade.detectMultiScale(gray, 1.3, 5, 0, minSize=(120, 120), maxSize=(350, 350))

        for (x, y, w, h) in faces:
            # ... (same as before)

            glass = cv2.resize(self.specs_ori, (w, sh_glass), interpolation=cv2.INTER_CUBIC)
            cigar = cv2.resize(self.cigar_ori, (w, sh_cigar), interpolation=cv2.INTER_CUBIC)
            mus = cv2.resize(self.mus_ori, (w, sh_mus), interpolation=cv2.INTER_CUBIC)

            transparentOverlay(frame[glass_symin:glass_symax, x:x + w], glass)
            transparentOverlay(frame[cigar_symin:cigar_symax, x:x + w], cigar)
            transparentOverlay(frame[mus_symin:mus_symax, x:x + w], mus)

        return frame

    def run(self):
        while self.cap.isOpened():
            result, frame = self.cap.read()
            if result:
                processed_frame = self.process_frame(frame)
                cv2.imshow("frame", processed_frame)
                if cv2.waitKey(1) == ord('q'):
                    break

        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    face_overlay = FaceOverlay()
    face_overlay.run()
