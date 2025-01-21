HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <title>Glance</title>
    <style>
        body {
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background: #292929;
            overflow: hidden;
        }
        .zoom-container {
            height: zooom_container_height;
            width: 100vw;
            position: relative;
            overflow: hidden;
            background: #000000;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
            cursor: grab;
        }
        .zoom-container:active {
            cursor: grabbing;
        }
        #zoomable-image {
            display: block;
            max-width: 100vw;
            max-height: 100vh;
            width: auto;
            height: auto;
            object-fit: contain;
            transform-origin: 0 0;
        }
        .controls {
            position: fixed;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.7);
            padding: 10px;
            border-radius: 20px;
            display: flex;
            gap: 10px;
        }
        button {
            background: white;
            border: none;
            padding: 8px 15px;
            border-radius: 15px;
            cursor: pointer;
            font-weight: bold;
        }
        button:hover {
            background: #eee;
        }
    </style>
</head>
<body id="zoom-body">
    <div class="zoom-container" id="zoom-container">
        <img id="zoomable-image" src="/api/placeholder/800/600" alt="Zoomable Image">
    </div>
    <div id="zoom-controls" class="controls">
        <button onclick="zoomIn()">Zoom In (+)</button>
        <button onclick="zoomOut()">Zoom Out (-)</button>
        <button onclick="resetZoom()">Reset</button>
    </div>

    <script>
        const container = document.querySelector('#zoom-container');
        const img = document.querySelector('#zoomable-image');
        let scale = 1;
        const maxScale = 50;
        let isDragging = false;
        let startPos = { x: 0, y: 0 };
        let currentPos = { x: 0, y: 0 };

        // Zoom functions
        function zoomIn() {
            scale = Math.min(scale * 1.2, maxScale);
            updateTransform();
        }

        function zoomOut() {
            scale = Math.max(scale / 1.2, 1);
            if (scale == 1){
                currentPos = { x: 0, y: 0 };
            }
            updateTransform();
        }

        function resetZoom() {
            scale = 1;
            currentPos = { x: 0, y: 0 };
            updateTransform();
        }

        function updateTransform() {
            img.style.transform = `translate(${currentPos.x}px, ${currentPos.y}px) scale(${scale})`;
        }

        // Mouse wheel zoom
        container.addEventListener('wheel', (e) => {
            e.preventDefault();

            if (e.deltaY < 0) {
                zoomIn();
            } else {
                zoomOut();
            }
        });

        // Drag functionality
        container.addEventListener('mousedown', (e) => {
            e.preventDefault();
            isDragging = true;
            startPos = {
                x: e.clientX - currentPos.x,
                y: e.clientY - currentPos.y
            };
            container.style.cursor = 'grabbing';
        });

        window.addEventListener('mousemove', (e) => {
            e.preventDefault();
            if (!isDragging) return;

            currentPos = {
                x: e.clientX - startPos.x,
                y: e.clientY - startPos.y
            };
            updateTransform();
        });

        window.addEventListener('mouseup', () => {
            isDragging = false;
            container.style.cursor = 'grab';
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

        document.addEventListener('DOMContentLoaded', function() {
            var element = document.getElementById(uniqueId);
            if (element) {  // Check if element exists
                element.addEventListener('click', function() {
                    this.style.color = 'red';
                    this.innerHTML = 'Clicked!';
                });
            }
        });
    </script>
</body>
</html>"""
