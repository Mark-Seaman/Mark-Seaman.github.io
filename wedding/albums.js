// Fill in each room's links once the Google Photos albums exist.
// name: the album title to create in Google Photos, one album per room
// album: the shared album link (Share > Create link in Google Photos)
// upload: the same link works for uploads when "Collaborate" is turned on
// form: optional Google Form link for written stories
const ROOMS = {
  "our-story":   { name: "Mark & Kim — Our Story", album: "https://photos.app.goo.gl/d7av1UvV8eubCi3o8", upload: "https://photos.app.goo.gl/d7av1UvV8eubCi3o8" },
  "the-weekend": { name: "Mark & Kim — The Weekend", album: "https://photos.app.goo.gl/jw7TfQV3NBcF4G9j9", upload: "https://photos.app.goo.gl/jw7TfQV3NBcF4G9j9" },
  "getting-ready": { name: "Mark & Kim — Getting Ready", album: "https://photos.app.goo.gl/R2MMVphdBG8m1CtW9", upload: "https://photos.app.goo.gl/R2MMVphdBG8m1CtW9" },
  "ceremony":    { name: "Mark & Kim — The Ceremony", album: "https://photos.app.goo.gl/wv6VXwttLKg5UyzB8", upload: "https://photos.app.goo.gl/wv6VXwttLKg5UyzB8" },
  "reception":   { name: "Mark & Kim — The Reception", album: "https://photos.app.goo.gl/3EWT61aiHQzo64MF7", upload: "https://photos.app.goo.gl/3EWT61aiHQzo64MF7" },
  "family":      { name: "Mark & Kim — Family", album: "https://photos.app.goo.gl/K4WFY9mztcJwoG8AA", upload: "https://photos.app.goo.gl/K4WFY9mztcJwoG8AA" },
  "guests":      { name: "Mark & Kim — Guest Photos", album: "https://photos.app.goo.gl/NjAZGJ2wMyJbt6xe6", upload: "https://photos.app.goo.gl/NjAZGJ2wMyJbt6xe6" },
  "honeymoon":   { name: "Mark & Kim — Honeymoon", album: "https://photos.app.goo.gl/J6SvdYmcaRN54aA68", upload: "https://photos.app.goo.gl/J6SvdYmcaRN54aA68" },
  "stories":     { name: "Mark & Kim — Stories and Wishes", album: "https://photos.app.goo.gl/YvtFp4Kx6kK9vGSUA", upload: "https://photos.app.goo.gl/YvtFp4Kx6kK9vGSUA", form: "" },
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
