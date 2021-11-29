import logo from './logo.svg';
import "bootstrap/dist/css/bootstrap.min.css";
import './App.css';

class App extends Component {
  render() {
    return (
      <div>
        <nav className="navbar navbar-expand navbar-dark bg-dark">
          <a href="/tutorials" className="navbar-brand">
            petProfile
          </a>
          <div className="navbar-nav mr-auto">
          <li className="nav-item">
              <Link to={"/home"} className="nav-link">
                Tutorials
              </Link>
            </li>
            <li className="nav-item">
              <Link to={"/signup"} className="nav-link">
                Tutorials
              </Link>
            </li>

            <li className="nav-item">
              <Link to={"/sigin"} className="nav-link">
                Add
              </Link>
            </li>
            <li className="nav-item">
              <Link to={"/signout"} className="nav-link">
                Add
              </Link>
            </li>
          </div>
        </nav>

        <div className="container mt-3">
          <Switch>
            <Route exact path={["/", "/home"]} component={Home} />
            <Route exact path="/signup" component={Register} />
            <Route path="/signin" component={Login} />
          </Switch>
        </div>
      </div>
    );
  }
}

export default App;
