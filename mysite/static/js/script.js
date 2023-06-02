$(document).ready(function () {
   $('#weather-form').submit(function (event) {
      event.preventDefault();

      var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();

      var city = $('#id_city').val();

      $.ajax({
         url: '/get_weather/',
         type: 'POST',
         data: {
            'city': city,
            'csrfmiddlewaretoken': csrfToken
         },
         success: function (response) {
            $('.weather-result').text(response.result);
         },
         error: function () {
            $('.weather-result').text('Не вдалося отримати дані');
         }
      });
   });
});

particlesJS("particles-js", {
   particles: {
      number: {
         value: 80,
         density: {
            enable: true,
            value_area: 800
         }
      },
      color: {
         value: "#ffffff"
      },
      shape: {
         type: "circle",
         stroke: {
            width: 0,
            color: "#000000"
         },
         polygon: {
            nb_sides: 5
         }
      },
      opacity: {
         value: 0.5,
         random: false,
         anim: {
            enable: false,
            speed: 1,
            opacity_min: 0.1,
            sync: false
         }
      },
      size: {
         value: 3,
         random: true,
         anim: {
            enable: false,
            speed: 40,
            size_min: 0.1,
            sync: false
         }
      },
      line_linked: {
         enable: true,
         distance: 150,
         color: "#ffffff",
         opacity: 0.4,
         width: 1
      },
      move: {
         enable: true,
         speed: 6,
         direction: "none",
         random: false,
         straight: false,
         out_mode: "out",
         bounce: false,
         attract: {
            enable: false,
            rotateX: 600,
            rotateY: 1200
         }
      }
   },
   interactivity: {
      detect_on: "canvas",
      events: {
         onhover: {
            enable: true,
            mode: "repulse"
         },
         onclick: {
            enable: true,
            mode: "push"
         },
         resize: true
      },
      modes: {
         grab: {
            distance: 400,
            line_linked: {
               opacity: 1
            }
         },
         bubble: {
            distance: 400,
            size: 40,
            duration: 2,
            opacity: 8,
            speed: 3
         },
         repulse: {
            distance: 200,
            duration: 0.4
         },
         push: {
            particles_nb: 4
         },
         remove: {
            particles_nb: 2
         }
      }
   },
   retina_detect: true
});

$(document).ready(function () {
   $('#fullpage').fullpage({
      // Налаштування fullPage.js
   });
});

//header
$(window).scroll(function () {
   if ($(this).scrollTop() > 0) {
      $('.transparent-header').addClass('scrolled');
   } else {
      $('.transparent-header').removeClass('scrolled');
   }
});
//check list
const taskList = document.getElementById('task-list');
const addTaskBtn = document.getElementById('add-task-btn');

addTaskBtn.addEventListener('click', function () {
   const taskCount = taskList.querySelectorAll('input[type="checkbox"]').length;
   const taskId = 'task' + (taskCount + 1);

   const taskInput = document.createElement('input');
   taskInput.setAttribute('type', 'checkbox');
   taskInput.setAttribute('id', taskId);

   const taskLabel = document.createElement('label');
   taskLabel.setAttribute('for', taskId);
   taskLabel.setAttribute('contenteditable', 'true');
   taskLabel.addEventListener('input', function () {
      saveTasks();
   });

   taskList.appendChild(taskInput);
   taskList.appendChild(taskLabel);

   saveTasks();
});

// Функція для збереження задач у локальному сховищі
function saveTasks() {
   const tasks = [];

   const taskInputs = taskList.querySelectorAll('input[type="checkbox"]');
   const taskLabels = taskList.querySelectorAll('label[contenteditable]');

   for (let i = 0; i < taskInputs.length; i++) {
      const task = {
         id: taskInputs[i].id,
         label: taskLabels[i].textContent,
         checked: taskInputs[i].checked
      };
      tasks.push(task);
   }

   localStorage.setItem('tasks', JSON.stringify(tasks));
}

// Функція для завантаження задач з локального сховища
function loadTasks() {
   const savedTasks = localStorage.getItem('tasks');

   if (savedTasks) {
      const tasks = JSON.parse(savedTasks);

      tasks.forEach(function (task) {
         const taskInput = document.createElement('input');
         taskInput.setAttribute('type', 'checkbox');
         taskInput.setAttribute('id', task.id);
         taskInput.checked = task.checked;

         const taskLabel = document.createElement('label');
         taskLabel.setAttribute('for', task.id);
         taskLabel.setAttribute('contenteditable', 'true');
         taskLabel.textContent = task.label;
         taskLabel.addEventListener('input', function () {
            saveTasks();
         });

         taskList.appendChild(taskInput);
         taskList.appendChild(taskLabel);
      });
   }
}

// Завантаження задач при завантаженні сторінки
loadTasks();
