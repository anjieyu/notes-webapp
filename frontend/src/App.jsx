import {render} from 'solid-js/web';
import {createSignal, onMount} from 'solid-js';
import './style.css';
 
function App() {

    return (
        <div>
            <h1>My Notes App</h1>
            <div class='app-container'>
                <p>Here is the notes app</p>
            </div>
        </div>
    );
};
render(() => <App />, document.getElementById('root'));