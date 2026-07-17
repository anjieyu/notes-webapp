import {render} from 'solid-js/web';
import {createSignal, onMount} from 'solid-js';
import {Notes} from './layouts/Notes';
import './style.css';
 
function App() {

    return (
        <div class='app'>
            <h1>My Notes App</h1>
            <div class='app-container'>
                <p>Here is the notes app</p>
                <Notes/>
            </div>
        </div>
    );
};
render(() => <App />, document.getElementById('root'));