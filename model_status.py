import os
import torch

CKPT_PATH = "/content/TITAN1_CANDIDATE_CHECKPOINT/TITAN1_R31_checkpoint.pt"

class Titan1Recovered(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.network = torch.nn.Sequential(
            torch.nn.Conv2d(1, 32, 3, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(32, 32, 3, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(32, 16, 3, padding=1),
            torch.nn.ReLU(),
            torch.nn.Conv2d(16, 1, 3, padding=1),
        )

    def forward(self, x):
        return self.network(x).clamp(0.0, 1.0)

def model_status():
    if not os.path.exists(CKPT_PATH):
        return {
            "status": "NOT_READY",
            "checkpoint": "MISSING",
            "inference": "FAILED",
            "detail": "Checkpoint file not found in candidate dir."
        }

    try:
        ckpt = torch.load(CKPT_PATH, map_location="cpu")
        state = ckpt["model_state_dict"]

        model = Titan1Recovered()
        model.load_state_dict(state, strict=True)
        model.eval()

        x = torch.rand(1, 1, 64, 64, dtype=torch.float32)
        with torch.no_grad():
            y = model(x)

        ok = (
            tuple(x.shape) == (1, 1, 64, 64)
            and tuple(y.shape) == (1, 1, 64, 64)
            and torch.isfinite(y).all()
            and float(y.min()) >= 0.0
            and float(y.max()) <= 1.0
        )

        if ok:
            return {
                "status": "READY",
                "checkpoint": "PRESENT",
                "inference": "PASS",
                "detail": "Candidate checkpoint loads and passes a minimal inference sanity check."
            }
        return {
            "status": "NOT_READY",
            "checkpoint": "PRESENT",
            "inference": "FAILED",
            "detail": "Checkpoint present but inference output invalid."
        }

    except Exception as e:
        return {
            "status": "NOT_READY",
            "checkpoint": "PRESENT",
            "inference": "FAILED",
            "detail": str(e)
        }

if __name__ == "__main__":
    print(model_status())
