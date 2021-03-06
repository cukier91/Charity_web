document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
  class Help {
    constructor($el) {
      this.$el = $el;
      this.$buttonsContainer = $el.querySelector(".help--buttons");
      this.$slidesContainers = $el.querySelectorAll(".help--slides");
      this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
      this.init();
    }

    init() {
      this.events();
    }

    events() {
      /**
       * Slide buttons
       */
      this.$buttonsContainer.addEventListener("click", e => {
        if (e.target.classList.contains("btn")) {
          this.changeSlide(e);
        }
      });

      /**
       * Pagination buttons
       */
      this.$el.addEventListener("click", e => {
        if (e.target.classList.contains("btn") && e.target.parentElement.parentElement.classList.contains("help--slides-pagination")) {
          this.changePage(e);
        }
      });
    }

    changeSlide(e) {
      e.preventDefault();
      const $btn = e.target;

      // Buttons Active class change
      [...this.$buttonsContainer.children].forEach(btn => btn.firstElementChild.classList.remove("active"));
      $btn.classList.add("active");

      // Current slide
      this.currentSlide = $btn.parentElement.dataset.id;

      // Slides active class change
      this.$slidesContainers.forEach(el => {
        el.classList.remove("active");

        if (el.dataset.id === this.currentSlide) {
          el.classList.add("active");
        }
      });
    }

    /**
     * TODO: callback to page change event
     */
    changePage(e) {
      e.preventDefault();
      const page = e.target.dataset.page;

      console.log(page);
    }
  }
  const helpSection = document.querySelector(".help");
  if (helpSection !== null) {
    new Help(helpSection);
  }

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });


  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      const hidder = document.getElementsByName('category')
      const category = document.getElementsByName('categories')

      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();


      category.forEach((e) =>{
        if (e.checked){
         hidder.forEach((f) =>{
           if(f.id !== e.value){
             f.parentElement.hidden = true
           }
         })
        }
      })
        });
      });


      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      const category = document.getElementsByName('categories')
      const user = document.getElementById('id_user')
      const quantity = document.getElementById('id_quantity')
      const institution = document.getElementsByName('institution')
      const address = document.getElementById('id_address')
      const city = document.getElementById('id_city')
      const postcode = document.getElementById('id_zip_code')
      const phone = document.getElementById('id_phone_no')
      const data = document.getElementById('id_pick_up_date')
      const time = document.getElementById('id_pick_up_time')
      const info = document.getElementById('id_pick_up_comment')
      const token = document.getElementsByName('csrfmiddlewaretoken')[0]

      const fd = new FormData()
        fd.append('quantity', quantity.value)
        fd.append('address', address.value)
        fd.append('city', city.value)
        fd.append('zip_code', postcode.value)
        fd.append('phone_no', phone.value)
        fd.append('pick_up_date', data.value)
        fd.append('pick_up_time', time.value)
        fd.append('pick_up_comment', info.value)
        fd.append('user', user.value)

            let count = 0;
      category.forEach((e) =>{
        if (e.checked){
          fd.append('categories', category[count].value)
          count++
        }
        else{
            count++
          }
      })

      let i = 0;
      institution.forEach((cb) =>{
        if (cb.checked){
          fd.append('institution', institution[i].value)
          i ++
        }
        else{
          i++
        }

      })



      fetch('/donation/', {
          credentials: 'include',
          method: 'POST',
          headers: {
            'Accept': 'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            'X-CSRFToken': token.value,
          },
          body: fd
        })
            .then(response => response.json())
            .then(result => {
              console.log(fd)
              console.log('Success:', result);
            })
            .catch(error => {
              console.log('Error:', error);
            })
      this.currentStep++;
      this.updateForm();




      // form.addEventListener('submit', e => {
      //   e.preventDefault()
      //
      //
      //
      //
      // })
    }

  }

  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }

});


const category = document.getElementsByName('categories')
const user = document.getElementById('id_user')
const quantity = document.getElementById('id_quantity')
const institution = document.getElementsByName('institution')
const address = document.getElementById('id_address')
const city = document.getElementById('id_city')
const postcode = document.getElementById('id_zip_code')
const phone = document.getElementById('id_phone_no')
const data = document.getElementById('id_pick_up_date')
const time = document.getElementById('id_pick_up_time')
const info = document.getElementById('id_pick_up_comment')


const street = document.getElementById("street")
const city_l = document.getElementById('city_l')
const code = document.getElementById('code')
const phone_l = document.getElementById('phone')
const bags = document.getElementById('bags')
const foundation = document.getElementById('foundation')
const data_l = document.getElementById('data')
const time_l = document.getElementById('time')
const info_l = document.getElementById('info')


arr = []
function myFunction() {
  street.innerHTML = address.value
  code.innerHTML = postcode.value
  phone_l.innerHTML = phone.value
  city_l.innerHTML = city.value
  data_l.innerHTML = data.value
  time_l.innerHTML = time.value
  info_l.innerHTML = info.value
  bags.innerHTML = quantity.value


    let i = 0;
      institution.forEach((cb) =>{
        if (cb.checked){
          arr.push(institution[i].value)
          i ++
        }
        else{
          i++
        }

      })
   foundation.innerHTML = document.getElementById(`institution_name_${arr[0]}`).innerText
}