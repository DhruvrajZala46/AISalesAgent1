# How a Short gets posted (works since 12 Nov 2026)

Full quality, nothing public in between, scheduled by YouTube itself.

1. **Open a private upload slot (Zapier).** YouTube app, "API Request (Beta)", mutating
   (`youtube_make_api_mutating_request`): `POST https://www.googleapis.com/upload/youtube/v3/videos` with query
   `uploadType=resumable`, `part=snippet,status`, headers `Content-Type: application/json; charset=UTF-8`,
   `X-Upload-Content-Type: video/mp4`, `X-Upload-Content-Length: <bytes>`, and the body:
   `{"snippet":{"title","description","tags":[...],"categoryId":"26","defaultLanguage":"en","defaultAudioLanguage":"en"},
   "status":{"privacyStatus":"private","publishAt":"<slot in UTC, e.g. 2026-11-12T17:30:00Z>","selfDeclaredMadeForKids":false,"embeddable":true}}`.
   The answer has a `location` header: the upload slot.
2. **Send the file into the slot (this machine).**
   `bash tools/yt_put.sh <..._final.mp4> "<location url>"`. It prints the video id and the publishAt YouTube kept.
3. **Check.** Zapier GET `videos?part=status,processingDetails,contentDetails&id=<id>`: processed, `hd`, private,
   the right publishAt. Then list the uploads playlist (`UU8RS6V8ua_-mD92kGitPCnQ`) for duplicates.

`publishAt` works on this channel (no partner status needed): the video stays private and goes public at the slot.

**If step 1 times out** (Zapier's 60 s limit), YouTube may still have made an empty video record (it did for #13:
`iGn-2wL_-Wk`, 0 s, now unscheduled and titled "EMPTY DUPLICATE - safe to delete"). Before retrying, list the
uploads playlist; after, unschedule any empty twin (PUT `videos?part=snippet,status` without publishAt). Deleting
is the user's call (Studio).

What did not work: litterbox.catbox.moe (HTTP 412 to this machine) and tmpfiles.org (the connection is cut during
the handshake from this cloud machine). Google Drive is connected in Zapier (fashionone227@gmail.com) as a spare
route.

**Measure the file right before step 1** (`stat -c %s file.mp4`) and put that exact number in
`X-Upload-Content-Length`. A rebuilt file has a new size; a wrong size makes step 2 fail with HTTP 400, and the
failed slot still leaves an empty private video (Taj Mahal, 14 Nov: `G4zo2VFSynE`, unscheduled and renamed at once).
After any failed or timed-out step, list the uploads playlist and unschedule the empty twin.
