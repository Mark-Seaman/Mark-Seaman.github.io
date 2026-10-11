// Fill in each room's links once the Google Photos albums exist.
// album: the shared album link (Share > Create link in Google Photos)
// upload: the same link works for uploads when "Collaborate" is turned on
// form: optional Google Form link for written stories
const ROOMS = {
  "our-story":   { album: "", upload: "" },
  "the-weekend": { album: "", upload: "" },
  "getting-ready": { album: "", upload: "" },
  "ceremony":    { album: "", upload: "" },
  "reception":   { album: "", upload: "" },
  "family":      { album: "", upload: "" },
  "guests":      { album: "", upload: "" },
  "honeymoon":   { album: "", upload: "" },
  "stories":     { album: "", upload: "", form: "" },
};

document.addEventListener("DOMContentLoaded", () => {
  const key = document.body.dataset.room;
  const links = ROOMS[key];
  if (!links) return;
  const set = (id, url, label) => {
    const el = document.getElementById(id);
    if (!el) return;
    if (url) {
      el.href = url;
      el.target = "_blank";
      el.rel = "noopener";
    } else {
      el.classList.remove("primary", "secondary");
      el.classList.add("pending");
      el.removeAttribute("href");
      el.textContent = label + " (coming soon)";
    }
  };
  set("view-album", links.album, "View the album");
  set("add-photos", links.upload, "Add your photos");
  set("share-story", links.form, "Share a story");
});
