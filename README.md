# Hyunkyu Kang — Academic Website

Personal academic website based on [Academic Pages](https://github.com/academicpages/academicpages.github.io).

- Website: https://khk0606.github.io
- CV: https://khk0606.github.io/files/CV_HyunkyuKang.pdf

## 수정할 파일

| 내용 | 파일 |
| --- | --- |
| 이름, 이메일, 소속, GitHub | `_config.yml` |
| 첫 화면 소개 | `_pages/about.md` |
| 연구 및 프로젝트 | `_pages/research.md` |
| CV 웹페이지 | `_pages/cv.md` |
| CV 원문 및 PDF 생성 | `cv/build_cv.py` |
| 메뉴 | `_data/navigation.yml` |

`main` 브랜치에 push하면 GitHub Actions가 Jekyll 사이트를 빌드하고 GitHub Pages에 배포합니다.
GitHub Settings → Pages → Source는 **GitHub Actions**를 사용합니다.
배포 전에 내부 링크, CV·이미지 파일, 템플릿 예시 문구 잔존 여부를 자동 검사합니다.

## 로컬 실행

Ruby 3.2 이상과 Bundler가 필요합니다.

```sh
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

## CV 재생성

Python 3와 ReportLab, Pillow가 필요합니다.

```sh
python3 -m pip install -r cv/requirements.txt
python3 cv/build_cv.py
```

결과는 `files/CV_HyunkyuKang.pdf`에 저장됩니다. CV와 웹페이지의 내용은 각각 수정해야 합니다.
학력 날짜·학점·수상·논문은 확인되지 않아 기재하지 않았습니다. 연구 프로젝트를 출판 논문으로 표시하지 않습니다.

## Attribution

Based on Academic Pages and Minimal Mistakes. Original license retained in `LICENSE`.
