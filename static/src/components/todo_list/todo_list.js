/** @odoo-module **/
import { registry } from '@web/core/registry';
const { Component, useState, onWillStart} = owl;
import { useService } from "@web/core/utils/hooks";

export class OwlTodo extends Component {
    setup(){
        this.state = useState({
            taskList:[],
            user: null
        })
        this.orm = useService("orm")
        this.model = "todo.list"

        onWillStart(async ()=>{
            await this.getAllTask()
        })
    }

    async getAllTask(){
        this.state.taskList = await this.orm.searchRead(this.model, [], ["name", "active", "color", "priority","date_time"])
    }

}

OwlTodo.template = 'owl_todo_app.Todo_list'
registry.category('actions').add('owl_todo_app.action_todo_list_js', OwlTodo);
