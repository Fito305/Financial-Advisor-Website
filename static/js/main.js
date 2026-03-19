const navToggle = document.querySelector(".nav-toggle");
const navMenu = document.querySelector(".nav-links");
const navLinks = document.querySelectorAll(".nav-links a");
const contactForm = document.querySelector("#contact-form");
const formStatus = document.querySelector("#form-status");

if (navToggle && navMenu) {
  navToggle.addEventListener("click", () => {
    const isOpen = navMenu.classList.toggle("is-open");
    navToggle.setAttribute("aria-expanded", String(isOpen));
  });

  navLinks.forEach((link) => {
    link.addEventListener("click", () => {
      navMenu.classList.remove("is-open");
      navToggle.setAttribute("aria-expanded", "false");
    });
  });
}

if (contactForm && formStatus) {
  contactForm.addEventListener("submit", async (event) => {
    event.preventDefault();

    formStatus.textContent = "";
    formStatus.classList.remove("is-success", "is-error", "has-warning");

    const submitButton = contactForm.querySelector("button[type='submit']");
    const defaultLabel = submitButton.dataset.defaultLabel || submitButton.textContent;
    const submittingLabel =
      submitButton.dataset.submittingLabel || "[Submitting Placeholder]";
    const formData = new FormData(contactForm);
    const payload = Object.fromEntries(formData.entries());

    if (!payload.name || !payload.email || !payload.phone) {
      formStatus.textContent = "Please complete all required fields.";
      formStatus.classList.add("is-error");
      return;
    }

    submitButton.disabled = true;
    submitButton.textContent = submittingLabel;

    try {
      const response = await fetch("/api/contact", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      const body = await response.json();

      if (!response.ok) {
        throw new Error(body.detail || "Unable to submit the form.");
      }

      formStatus.textContent = body.message;
      formStatus.classList.add("is-success");
      if (body.warning) {
        formStatus.textContent = `${body.message} ${body.warning}`;
        formStatus.classList.add("has-warning");
      }
      contactForm.reset();
    } catch (error) {
      formStatus.textContent = error.message;
      formStatus.classList.add("is-error");
    } finally {
      submitButton.disabled = false;
      submitButton.textContent = defaultLabel;
    }
  });
}
