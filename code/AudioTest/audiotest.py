import winsound
# Play Windows exit sound.
winsound.PlaySound("SystemHand", winsound.SND_ALIAS)

# Probably play Windows default sound, if any is registered (because
# "*" probably isn't the registered name of any sound).
winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)