HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <script src="https://unpkg.com/lucide@latest"></script>
    <title>Gawp</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: auto;
        }
        img {
            position: absolute;
            width: auto;
            height: auto;
            object-fit: contain;
        }
        .button-container {
            position: absolute;
            right: 20px;
            top: 50%;
            transform: translateY(-50%);
            display: flex;
            flex-direction: column;
            gap: 10px;
            z-index: 1;
        }
        button {
            padding: 10px;
            border: none;
            border-radius: 5px;
            background-color: #007bff;
            color: white;
            cursor: pointer;
            transition: background-color 0.2s;
            width: 40px;
            height: 40px;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        button:hover {
            background: #eee;
        }
        .lucide {
            width: 20px;
            height: 20px;
            stroke: white;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
            fill: none;
        }
        /* Icon styling */
        svg {
            width: 20px;
            height: 20px;
            stroke: white;
            stroke-width: 2;
            stroke-linecap: round;
            stroke-linejoin: round;
            fill: none;
        }
    </style>
</head>
<body id="zoom-body">
    <img id="image" src="/api/placeholder/800/600" alt="Zoomable Image">
    <div class="button-container">
        <button id="home-button" onclick="resetZoom()">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                <polyline points="9 22 9 12 15 12 15 22"/>
            </svg>
        </button>
        <button id="plus-button" onclick="zoomIn()">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <line x1="12" y1="5" x2="12" y2="19"/>
                <line x1="5" y1="12" x2="19" y2="12"/>
            </svg>
        </button>
        <button id="minus-button" onclick="zoomOut()">
            <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                <line x1="5" y1="12" x2="19" y2="12"/>
            </svg>
        </button>
    </div>

    <script>
        // const container = document.querySelector('#image_container');
        const img = document.querySelector('#image');
        const imgOriginalPosition = {
            x: img.getBoundingClientRect().x,
            y: img.getBoundingClientRect().y
        }
        let scale = 1;
        let isDragging = false;
        let startPos = { x: 0, y: 0 };
        let currentPos = { x: 0, y: 0 };

        // Zoom functions
        function zoomIn() {
            updateImage(1.2, img.getBoundingClientRect().x, img.getBoundingClientRect().y)
        }

        function zoomOut() {
            updateImage(1/1.2, img.getBoundingClientRect().x, img.getBoundingClientRect().y)
        }

        function resetZoom() {
            let currImgScale = img.getBoundingClientRect().width / img.naturalWidth;
            scale = 1;
            currentPos = { x: 0, y: 0 };
            updateImage(1/currImgScale, imgOriginalPosition.x, imgOriginalPosition.y)
        }

        function updateImage(scale, x, y) {
            let w = img.getBoundingClientRect().width;
            let h = img.getBoundingClientRect().height;
            img.style.width = `${w * scale}px`;
            img.style.height = `${h * scale}px`;
            img.style.top = `${y}px`;
            img.style.left = `${x}px`;
        }

        // Mouse wheel zoom
        img.addEventListener('wheel', (e) => {
            e.preventDefault();
            let scaling = e.deltaY < 0 ? 1.2 : 1 / 1.2;
            let currImgScale = img.getBoundingClientRect().width / img.naturalWidth;
            let nextImgScale = currImgScale * scaling;
            let currImgPos = {
                x: img.getBoundingClientRect().x,
                y: img.getBoundingClientRect().y
            };
            let nextImgPos = {
                x: currImgPos.x - img.width*(nextImgScale - currImgScale)/2,
                y: currImgPos.y - img.height*(nextImgScale - currImgScale)/2
            };
            let currCursPos = {
                x: e.clientX,
                y: e.clientY
            };
            let m1 = {
                    x: -currImgPos.x + currCursPos.x,
                    y: -currImgPos.y + currCursPos.y
                }
            let m2 = {
                x: m1.x*scaling,
                y: m1.y*scaling
            }
            updateImage(
                    scaling,
                    currImgPos.x + m1.x - m2.x,
                    currImgPos.y + m1.y - m2.y
                );
        });

        // Drag functionality
        img.addEventListener('mousedown', (e) => {
            e.preventDefault();
            isDragging = true;
            let currImgPos = {
                x: img.getBoundingClientRect().x,
                y: img.getBoundingClientRect().y
            };
            startPos = {
                x: e.clientX - currImgPos.x,
                y: e.clientY - currImgPos.y
            };
            img.style.cursor = 'grabbing';
        });

        window.addEventListener('mousemove', (e) => {
            e.preventDefault();
            if (!isDragging) return;

            currentPos = {
                x: e.clientX - startPos.x,
                y: e.clientY - startPos.y
            };
            updateImage(1, currentPos.x, currentPos.y);
        });

        window.addEventListener('mouseup', () => {
            isDragging = false;
            img.style.cursor = 'grab';
        });

        // Keyboard controls
        document.addEventListener('keydown', (e) => {
            switch(e.key) {
                case '+':
                case '=':
                    zoomIn();
                    break;
                case '-':
                case '_':
                    zoomOut();
                    break;
                case '0':
                    resetZoom();
                    break;
            }
        });
    </script>
</body>
</html>"""
