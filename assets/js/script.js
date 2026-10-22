'use strict';

// Small, defensive helpers keep the page functional if an optional element is absent.
const elementToggleFunc = (elem) => {
  if (elem) elem.classList.toggle("active");
};

// Sidebar toggle (mobile).
const sidebar = document.querySelector("[data-sidebar]");
const sidebarBtn = document.querySelector("[data-sidebar-btn]");
if (sidebarBtn && sidebar) {
  sidebarBtn.addEventListener("click", () => elementToggleFunc(sidebar));
}

// Quote cards and modal.
const testimonialsItem = document.querySelectorAll("[data-testimonials-item]");
const modalContainer = document.querySelector("[data-modal-container]");
const modalCloseBtn = document.querySelector("[data-modal-close-btn]");
const overlay = document.querySelector("[data-overlay]");
const modalImg = document.querySelector("[data-modal-img]");
const modalTitle = document.querySelector("[data-modal-title]");
const modalText = document.querySelector("[data-modal-text]");

const testimonialsModalFunc = () => {
  elementToggleFunc(modalContainer);
  elementToggleFunc(overlay);
};

testimonialsItem.forEach((item) => {
  item.addEventListener("click", () => {
    const avatar = item.querySelector("[data-testimonials-avatar]");
    const title = item.querySelector("[data-testimonials-title]");
    const text = item.querySelector("[data-testimonials-text]");
    if (avatar && modalImg) {
      modalImg.src = avatar.src;
      modalImg.alt = avatar.alt;
    }
    if (title && modalTitle) modalTitle.textContent = title.textContent.trim();
    if (text && modalText) modalText.innerHTML = text.innerHTML;
    testimonialsModalFunc();
  });
});
if (modalCloseBtn) modalCloseBtn.addEventListener("click", testimonialsModalFunc);
if (overlay) overlay.addEventListener("click", testimonialsModalFunc);

// Portfolio filtering uses the same lower-case category names on desktop and mobile.
const select = document.querySelector("[data-select]");
const selectItems = document.querySelectorAll("[data-select-item]");
const selectValue = document.querySelector("[data-selecct-value]");
const filterBtn = document.querySelectorAll("[data-filter-btn]");
const filterItems = document.querySelectorAll("[data-filter-item]");

const filterFunc = (selectedValue) => {
  filterItems.forEach((item) => {
    const category = (item.dataset.category || "").toLowerCase();
    const show = selectedValue === "all" || selectedValue === category;
    item.classList.toggle("active", show);
  });
};

if (select) select.addEventListener("click", () => elementToggleFunc(select));
selectItems.forEach((item) => {
  item.addEventListener("click", () => {
    const selectedValue = item.textContent.trim().toLowerCase();
    if (selectValue) selectValue.textContent = item.textContent.trim();
    elementToggleFunc(select);
    filterFunc(selectedValue);
  });
});

let lastClickedBtn = null;
filterBtn.forEach((button) => {
  button.addEventListener("click", () => {
    const selectedValue = button.textContent.trim().toLowerCase();
    if (selectValue) selectValue.textContent = button.textContent.trim();
    filterFunc(selectedValue);
    if (lastClickedBtn) lastClickedBtn.classList.remove("active");
    button.classList.add("active");
    lastClickedBtn = button;
  });
});

// Contact form validation, if a form is present on the page.
const form = document.querySelector("[data-form]");
const formInputs = document.querySelectorAll("[data-form-input]");
const formBtn = document.querySelector("[data-form-btn]");
if (form && formBtn) {
  formInputs.forEach((input) => {
    input.addEventListener("input", () => {
      formBtn.disabled = !form.checkValidity();
    });
  });
}

// Page navigation: match the clicked link to the page by data-page, not by array index.
const navigationLinks = document.querySelectorAll("[data-nav-link]");
const pages = document.querySelectorAll("[data-page]");
navigationLinks.forEach((link) => {
  link.addEventListener("click", () => {
    const target = link.textContent.trim().toLowerCase();
    pages.forEach((page) => page.classList.toggle("active", page.dataset.page === target));
    navigationLinks.forEach((navLink) => navLink.classList.toggle("active", navLink === link));
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});
