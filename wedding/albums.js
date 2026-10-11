// Fill in each room's links once the Google Photos albums exist.
// name: the album title to create in Google Photos, one album per room
// album: the shared album link (Share > Create link in Google Photos)
// upload: the same link works for uploads when "Collaborate" is turned on
// form: optional Google Form link for written stories
const ROOMS = {
  "our-story":   { name: "Mark & Kim — Our Story", album: "", upload: "" },
  "the-weekend": { name: "Mark & Kim — The Weekend", album: "", upload: "" },
  "getting-ready": { name: "Mark & Kim — Getting Ready", album: "", upload: "" },
  "ceremony":    { name: "Mark & Kim — The Ceremony", album: "", upload: "" },
  "reception":   { name: "Mark & Kim — The Reception", album: "", upload: "" },
  "family":      { name: "Mark & Kim — Family", album: "", upload: "" },
  "guests":      { name: "Mark & Kim — Guest Photos", album: "", upload: "" },
  "honeymoon":   { name: "Mark & Kim — Honeymoon", album: "", upload: "" },
  "stories":     { name: "Mark & Kim — Stories and Wishes", album: "", upload: "", form: "" },
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
