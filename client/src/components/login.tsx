import * as React from "react";
import * as _ from "lodash";
import {Button, ButtonToolbar, FormGroup, FormControl, ControlLabel, HelpBlock} from "react-bootstrap";
import * as Cookies from 'js-cookie';

import {ProjectModel} from "../models/project";
import Experiments from "../containers/experiments";
import Groups from "../containers/groups";


export interface Props {
  fetchToken: (username: string, password: string) => any;
  history: any;
}


export default class Login extends React.Component<Props, Object> {
  componentDidMount() {
    const {fetchToken, history} = this.props;
  }
  
  public handleSubmit(event: any) {
    event.preventDefault();
    let username = (document.getElementById('username') as HTMLInputElement).value;
    let password = (document.getElementById('password') as HTMLInputElement).value;
    
    this.props.fetchToken(username, password).then((resp: any) => {
      Cookies.set('token', resp.token.token);
      Cookies.set('user', resp.username);
      this.props.history.push( `/${username}/`);
    }).catch((err: string) => {
      (document.getElementById('error-message') as HTMLElement).innerHTML = 'Unable to log in with provided credentials.';
    });
  }
  
  public render () {
    return (
      <div className="row">
         <div className="col-md-4 col-md-offset-4">
            <div className="login">
              <form onSubmit={this.handleSubmit.bind(this)}>
                <div className="form-group">
                  <label>Username or Email</label>
                  <input type="text" className="form-control" id="username" placeholder="Username"/>
                </div>
                <div className="form-group">
                  <label>Password</label>
                  <input type="password" className="form-control" id="password"/>
                </div>
                <div className="submit">
                    <input type="submit" value="Login" className="button btn btn-polyaxon" />
                </div>
                <div className="bg-danger error-message" id="error-message"></div>
              </form>
            </div>
         </div>
      </div>
    )
  }

}