import 'vite/modulepreload-polyfill';
import './styles/main.scss';
import * as bootstrap from 'bootstrap';
import Alpine from 'alpinejs';

window.Alpine = Alpine;
Alpine.start();
