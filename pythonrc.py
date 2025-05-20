"""
Might cause a PermissionError if the PYTHONSTARTUP env var points to this file and this file is inside a OneDrive directory.
In that case, consider making a copy of this in a local directory outside OneDrive, and having PYTHONSTARTUP point to that copy.
Other solutions may be possible, but would involve
changing OneDrive settings and I don't want to do that over something where the stakes are so low.
"""

def q():
	quit()