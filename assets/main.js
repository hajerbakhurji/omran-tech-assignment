document.documentElement.classList.add("js");

const isArabic = document.documentElement.dir === "rtl";
const reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;


// Header gets a dark background after scrolling a bit
const header = document.querySelector(".site-header");

function updateHeader() {
  header.classList.toggle("is-solid", window.scrollY > 40);
}
updateHeader();
window.addEventListener("scroll", updateHeader, { passive: true });


// Mobile menu
const menuButton = document.querySelector(".nav-toggle");

function setMenu(open) {
  document.body.classList.toggle("nav-open", open);
  menuButton.setAttribute("aria-expanded", open);
  menuButton.setAttribute("aria-label", open ? menuButton.dataset.close : menuButton.dataset.open);
}

menuButton.addEventListener("click", () => {
  setMenu(!document.body.classList.contains("nav-open"));
});

document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") setMenu(false);
});

document.querySelectorAll(".mobile-nav a").forEach((link) => {
  link.addEventListener("click", () => setMenu(false));
});


// Fade sections in when they scroll into view
const fadeItems = document.querySelectorAll(".reveal");

if (reduceMotion) {
  fadeItems.forEach((el) => el.classList.add("in"));
} else {
  const fadeObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        fadeObserver.unobserve(entry.target);
      }
    });
  }, { rootMargin: "0px 0px -8% 0px" });

  fadeItems.forEach((el) => fadeObserver.observe(el));
}


// Count up the numbers in the hero
function countUp(el) {
  const target = Number(el.dataset.count);
  const start = performance.now();
  const duration = 1400;

  function step(now) {
    const progress = Math.min((now - start) / duration, 1);
    const eased = 1 - Math.pow(1 - progress, 3);
    el.textContent = Math.round(target * eased);
    if (progress < 1) requestAnimationFrame(step);
  }
  requestAnimationFrame(step);
}

if (!reduceMotion) {
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        countUp(entry.target);
        counterObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.6 });

  document.querySelectorAll("[data-count]").forEach((el) => counterObserver.observe(el));
}


// Project filters
const filterBar = document.querySelector("[data-filters]");

if (filterBar) {
  const cards = document.querySelectorAll("[data-tags]");

  function showProjects(tag) {
    filterBar.querySelectorAll(".filter-btn").forEach((btn) => {
      btn.setAttribute("aria-pressed", btn.dataset.filter === tag);
    });
    cards.forEach((card) => {
      const tags = card.dataset.tags.split(" ");
      card.hidden = tag !== "all" && !tags.includes(tag);
    });
    history.replaceState(null, "", tag === "all" ? location.pathname : "#" + tag);
  }

  filterBar.addEventListener("click", (e) => {
    const btn = e.target.closest(".filter-btn");
    if (btn) showProjects(btn.dataset.filter);
  });

  // open with a filter from the link, e.g. projects.html#fuel
  const tagFromLink = location.hash.slice(1);
  if (tagFromLink && filterBar.querySelector(`[data-filter="${tagFromLink}"]`)) {
    showProjects(tagFromLink);
  }
}


// Image viewer for galleries and certificates
const imageButtons = document.querySelectorAll("[data-lightbox]");

if (imageButtons.length) {
  const viewer = document.createElement("div");
  viewer.className = "lightbox";
  viewer.setAttribute("role", "dialog");
  viewer.setAttribute("aria-modal", "true");
  viewer.innerHTML = `
    <img alt="">
    <button class="lb-btn lb-close" aria-label="Close">✕</button>
    <button class="lb-btn lb-prev" aria-label="Previous">‹</button>
    <button class="lb-btn lb-next" aria-label="Next">›</button>
    <div class="lb-count"></div>`;
  document.body.appendChild(viewer);

  const viewerImage = viewer.querySelector("img");
  const counter = viewer.querySelector(".lb-count");
  let group = [];
  let current = 0;
  let openedFrom = null;

  function showImage(index) {
    current = (index + group.length) % group.length;
    viewerImage.src = group[current].dataset.full;
    viewerImage.alt = group[current].dataset.alt || "";
    counter.textContent = `${current + 1} / ${group.length}`;
    viewer.querySelector(".lb-prev").hidden = group.length < 2;
    viewer.querySelector(".lb-next").hidden = group.length < 2;
  }

  function openViewer(button) {
    group = [...document.querySelectorAll(`[data-lightbox="${button.dataset.lightbox}"]`)];
    openedFrom = button;
    viewer.classList.add("open");
    document.body.style.overflow = "hidden";
    showImage(group.indexOf(button));
    viewer.querySelector(".lb-close").focus();
  }

  function closeViewer() {
    viewer.classList.remove("open");
    document.body.style.overflow = "";
    viewerImage.src = "";
    if (openedFrom) openedFrom.focus();
  }

  imageButtons.forEach((btn) => btn.addEventListener("click", () => openViewer(btn)));
  viewer.querySelector(".lb-close").addEventListener("click", closeViewer);
  viewer.querySelector(".lb-prev").addEventListener("click", () => showImage(current - 1));
  viewer.querySelector(".lb-next").addEventListener("click", () => showImage(current + 1));
  viewer.addEventListener("click", (e) => {
    if (e.target === viewer) closeViewer();
  });

  document.addEventListener("keydown", (e) => {
    if (!viewer.classList.contains("open")) return;
    if (e.key === "Escape") closeViewer();
    if (e.key === "ArrowRight") showImage(current + (isArabic ? -1 : 1));
    if (e.key === "ArrowLeft") showImage(current + (isArabic ? 1 : -1));
  });
}


// Contact page tabs
const tabs = [...document.querySelectorAll('[role="tab"]')];

function selectTab(tab) {
  tabs.forEach((t) => {
    const selected = t === tab;
    t.setAttribute("aria-selected", selected);
    t.tabIndex = selected ? 0 : -1;
    document.getElementById(t.getAttribute("aria-controls")).hidden = !selected;
  });
}

tabs.forEach((tab, i) => {
  tab.addEventListener("click", () => selectTab(tab));
  tab.addEventListener("keydown", (e) => {
    const step = isArabic ? -1 : 1;
    let next = null;
    if (e.key === "ArrowRight") next = tabs[(i + step + tabs.length) % tabs.length];
    if (e.key === "ArrowLeft") next = tabs[(i - step + tabs.length) % tabs.length];
    if (next) {
      selectTab(next);
      next.focus();
    }
  });
});

// open a tab from the link, e.g. contact.html#lgs
const tabFromLink = tabs.find((t) => t.dataset.key === location.hash.slice(1));
if (tabFromLink) selectTab(tabFromLink);


// Contact forms: for now they open the visitor's email app with the answers filled in.
// Later this can be connected to a form service.
document.querySelectorAll("form[data-mailto]").forEach((form) => {
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    if (!form.reportValidity()) return;

    const lines = [];
    form.querySelectorAll("input, select, textarea").forEach((field) => {
      if (!field.value) return;
      if (field.type === "radio" && !field.checked) return;
      const label = field.closest(".field").querySelector("label, legend");
      lines.push(`${label.textContent.trim()}: ${field.value}`);
    });

    const subject = encodeURIComponent(form.dataset.subject);
    const body = encodeURIComponent(lines.join("\n"));
    window.location.href = `mailto:${form.dataset.mailto}?subject=${subject}&body=${body}`;
  });
});


// Play the LGS video only while it's on screen
document.querySelectorAll("video[data-autoplay]").forEach((video) => {
  if (reduceMotion) {
    video.controls = true;
    return;
  }
  new IntersectionObserver((entries) => {
    if (entries[0].isIntersecting) {
      video.play().catch(() => {});
    } else {
      video.pause();
    }
  }, { threshold: 0.25 }).observe(video);
});


// AI assistant chat (ai.html)
// The browser only talks to our own server at /api/chat. The server talks to Claude.
const chatForm = document.getElementById("chat-form");

if (chatForm) {
  const settings = JSON.parse(document.getElementById("chat-settings").textContent);
  const messageList = document.getElementById("chat-messages");
  const input = document.getElementById("chat-input");
  const sendButton = chatForm.querySelector(".chat-send");
  const suggestions = document.getElementById("chat-suggestions");
  const questionsLeft = document.getElementById("chat-left");
  const welcomeMessage = messageList.innerHTML;

  let history = [];   // the conversation so far, sent with every question
  let waiting = false;

  function addMessage(text, type) {
    const bubble = document.createElement("div");
    bubble.className = "chat-msg chat-msg--" + type;
    bubble.textContent = text;   // textContent (not innerHTML) so an answer can never inject HTML
    messageList.appendChild(bubble);
    messageList.scrollTop = messageList.scrollHeight;
    return bubble;
  }

  function questionsAsked() {
    return history.filter((m) => m.role === "user").length;
  }

  async function ask(question) {
    question = question.trim();
    if (!question || waiting) return;

    if (questionsAsked() >= settings.maxQuestions) {
      addMessage(settings.errors.limit_reached, "error");
      return;
    }

    addMessage(question, "user");
    suggestions.hidden = true;
    input.value = "";
    input.style.height = "";
    waiting = true;
    sendButton.disabled = true;

    const typing = addMessage("", "bot");
    typing.classList.add("chat-typing");
    typing.innerHTML = "<i></i><i></i><i></i>";

    const messages = [...history, { role: "user", content: question }];
    let reply = null;
    let error = "default";

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ messages }),
      });
      const data = await response.json();
      if (data.reply) reply = data.reply;
      else if (data.error) error = data.error;
    } catch (e) {
      // no server (for example on GitHub Pages) or no internet
    }

    typing.remove();
    if (reply) {
      history = [...messages, { role: "assistant", content: reply }];
      addMessage(reply, "bot");
    } else {
      addMessage(settings.errors[error] || settings.errors.default, "error");
    }

    questionsLeft.textContent = settings.maxQuestions - questionsAsked();
    waiting = false;
    sendButton.disabled = false;
    input.focus();
  }

  chatForm.addEventListener("submit", (e) => {
    e.preventDefault();
    ask(input.value);
  });

  // Enter sends, Shift+Enter adds a new line
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter" && !e.shiftKey) {
      e.preventDefault();
      ask(input.value);
    }
  });

  // the text box grows with the question
  input.addEventListener("input", () => {
    input.style.height = "";
    input.style.height = Math.min(input.scrollHeight, 160) + "px";
  });

  suggestions.querySelectorAll(".chat-chip").forEach((chip) => {
    chip.addEventListener("click", () => ask(chip.textContent));
  });

  document.getElementById("chat-new").addEventListener("click", () => {
    history = [];
    messageList.innerHTML = welcomeMessage;
    suggestions.hidden = false;
    questionsLeft.textContent = settings.maxQuestions;
    input.focus();
  });
}


document.getElementById("year").textContent = new Date().getFullYear();
