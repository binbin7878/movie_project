const date = new Date();
// console.log(date.getFullYear());
const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0);
const reserveDate = document.querySelector('.reserve-date');
const theaterPlace = document.querySelectorAll('.theater-place');
const reserveTimeWant = document.querySelectorAll('.reserve-time-want');
const inputTitle = document.querySelector('.title');
const inputSelectedTheater = document.querySelector('.selectedTheater');
const inputReserveDate = document.querySelector('.reserveDate');
const inputRunningTime = document.querySelector('.runningTime');
const moveSeatForm = document.querySelector('.moveSeatForm');
const moveSeatButton = document.querySelector('.moveSeatButton');




let year = 0;
let month = 0;
add();
document.addEventListener('DOMContentLoaded', () => {
    add();
    addDate();
});

// 데이터 가져오기
function add() {
    $.ajax({
        url: '/movie/get_movies/',  // Django에서 추가한 API URL
        type: 'get',
        success: function(data) {
            // 여기서 data를 활용하여 필요한 처리를 수행
            console.log(data);

            // 예시: 영화 제목을 출력하는 함수 호출
            displayMovieTitles(data);

            
        },
        error: function() {
            // 에러 처리
            console.error('데이터를 가져오는 데 실패했습니다.');
        },
        
    });
}



// 예시: 영화 제목을 출력하는 함수
function displayMovieTitles(data) {
    const movieTitleWrapper = document.querySelector('.movie-list-title-wrapper');

    movieTitleWrapper.innerHTML = '';

    if (data && data.movies && Array.isArray(data.movies)) {
        const compareByTitle = (a, b) => a.title.localeCompare(b.title);
        const sortedMovies = data.movies.slice().sort(compareByTitle);

        sortedMovies.forEach(movie => {
            const buttonWrapper = document.createElement('div');
            buttonWrapper.classList.add('movie-list-title'); // 부모 div에 클래스 추가

            const button = document.createElement('button');
            button.classList.add('movie-title-button');
            button.innerText = movie.title;

            buttonWrapper.appendChild(button);
            movieTitleWrapper.appendChild(buttonWrapper);

            // 클릭 이벤트를 바로 설정
            button.addEventListener('click', function () {
                handleMovieTitleClick(button, movie);
            });
        });

        // 정렬 버튼 추가
        const sortWrapper = document.querySelector('.sort-wrapper');
        sortWrapper.innerHTML = `
            <div class="sort-rate">예매율순</div>
            <div class="sort-korean sort-selected">가나다순</div>
        `;

        // 정렬 버튼 클릭 이벤트 처리
        const sortButtons = document.querySelectorAll('.sort-wrapper div');
        sortButtons.forEach(button => {
            button.addEventListener('click', function() {
                // 클릭한 버튼에 대한 정렬 처리
                const sortBy = button.classList.contains('sort-rate') ? '예매율순' : '가나다순';
                console.log(`정렬 기준: ${sortBy}`);

                sortedMovies.sort(compareByTitle);

                movieTitleWrapper.innerHTML = '';

                sortedMovies.forEach(movie => {
                    const buttonWrapper = document.createElement('div');
                    buttonWrapper.classList.add('movie-list-title'); // 부모 div에 클래스 추가

                    const button = document.createElement('button');
                    button.classList.add('movie-title-button');
                    button.innerText = movie.title;

                    buttonWrapper.appendChild(button);
                    movieTitleWrapper.appendChild(buttonWrapper);

                    // 클릭 이벤트를 바로 설정
                    button.addEventListener('click', function () {
                        handleMovieTitleClick(button, movie);
                    });
                });

                sortButtons.forEach(btn => {
                    btn.classList.remove('sort-selected');
                });
                button.classList.add('sort-selected');
            });
        });
    } else {
        console.error('올바른 데이터를 가져오지 못했습니다.');
    }
}

// 영화 제목이 클릭되었을 때 처리하는 함수
function handleMovieTitleClick(button, movie) {
    const movieTitleButtons = document.querySelectorAll('.movie-title-button');
    movieTitleButtons.forEach(btn => {
        btn.classList.remove('movie-title-button-active');
    });
    button.classList.add('movie-title-button-active');
    console.log(button.innerText);
    console.log(movie.title);
    
    // form에 넘기기 위한
    
    inputTitle.value = button.innerText;

}






function setData(data) {
    data = JSON.parse(data);

    return data;
}

function setList(data) {
    document.querySelector('.movie-list-wrapper').innerHTML = JSON.parse(
        data
    ).reduce((html = '', item, index = 0) => {
        html += getMovieList(item);

        return html;
    }, ' ');
}



function addDate() {
    const weekOfDay = ['일', '월', '화', '수', '목', '금', '토'];
    const date = new Date(); // 현재 날짜를 가져옵니다.
    const year = date.getFullYear(); // 현재 연도를 가져옵니다.
    const month = date.getMonth() + 1; // 현재 월을 가져오고 1을 더합니다.
    const reserveDate = document.querySelector('.reserve-date');

    // 년도와 월 표시
    const yearMonthTitle = document.createElement('div');
    yearMonthTitle.classList = 'year-month-title';
    yearMonthTitle.innerHTML = `${year}/${month}`;
    reserveDate.append(yearMonthTitle);

    for (let i = 0; i < 30; i++) {
        const currentDate = new Date(year, month - 1, date.getDate() + i);
        const button = document.createElement('button');
        const spanWeekOfDay = document.createElement('span');
        const spanDay = document.createElement('span');

        button.classList = 'movie-date-wrapper';
        spanWeekOfDay.classList = 'movie-week-of-day';
        spanDay.classList = 'movie-day';

        const dayOfWeek = weekOfDay[currentDate.getDay()]; // 현재 날짜의 요일을 가져옵니다.

        if (dayOfWeek === '토') {
            spanWeekOfDay.classList.add('saturday');
            spanDay.classList.add('saturday');
        } else if (dayOfWeek === '일') {
            spanWeekOfDay.classList.add('sunday');
            spanDay.classList.add('sunday');
        }
        spanWeekOfDay.innerHTML = dayOfWeek;
        button.append(spanWeekOfDay);

        spanDay.innerHTML = currentDate.getDate();
        button.append(spanDay);

        reserveDate.append(button);

        dayClickEvent(button);
    }
}






function dayClickEvent(button) {
    button.addEventListener('click', function() {
        const movieDateWrapperActive = document.querySelectorAll(
            '.movie-date-wrapper-active'
        );
        movieDateWrapperActive.forEach(list => {
            list.classList.remove('movie-date-wrapper-active');
        });
        button.classList.add('movie-date-wrapper-active');
        console.log(button.childNodes[1].innerHTML);
        inputReserveDate.value =
            year +
            '.' +
            month +
            '.' +
            button.childNodes[1].innerHTML +
            '(' +
            button.childNodes[0].innerHTML +
            ')';
        console.log(inputReserveDate.value);
    });
}


theaterPlace.forEach(list => {
    list.addEventListener('click', function() {
        const theaterPlaceWrapper = document.querySelectorAll(
            '.theater-place-active'
        );
        theaterPlaceWrapper.forEach(li => {
            li.classList.remove('theater-place-active');
        });
        list.classList.add('theater-place-active');
        console.log(list.innerHTML);
        inputSelectedTheater.value = list.innerHTML;
    });
});


reserveTimeWant.forEach(list => {
    list.addEventListener('click', function() {
        const reserveTimeActive = document.querySelectorAll('.reserve-time-active');
        reserveTimeActive.forEach(li => {
            li.classList.remove('reserve-time-active');
        });
        list.classList.add('reserve-time-active');
        console.log(list.innerHTML);
        inputRunningTime.value = list.innerHTML;
    });
});

moveSeatButton.addEventListener('click', function() {
    if (!!inputTitle.value &&
        !!inputSelectedTheater.value &&
        !!inputReserveDate.value &&
        !!inputRunningTime.value
    ) {
        moveSeatForm.submit();
    } else {
        toastr.options = {
            positionClass: 'toast-top-full-width',
            progressBar: true,
            timeOut: 1000,
        };
        toastr.error(
            '<div style="color:white">모든 항목을 체크해 주세요</div>',
            '<div style="color:white">경고</div>', {
                timeOut: 3000,
            }
        );
    }
});

function sendForm(){
    var title=document.querySelector('.movie-title-button').innerText;
    var selectedTheater=document.querySelector('.theater-place:first-child').innerText;
    var reserveDate=document.querySelector('.movie-date-wrapper').value;
    var runningTime=document.querySelector('.runningTime').value;

    var form=document.querySelector('.movieSeatForm');

    form.querySelector('.title').value = title;
    form.querySelector('.selectedTheater').value = selectedTheater;
    form.querySelector('.movieDate').value = reserveDate;
    form.querySelector('.runningTime').value = runningTime;

    form.submit();
}