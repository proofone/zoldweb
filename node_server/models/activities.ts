

interface BaseActivity {
    creator_id: string
    parent_id?: string
    title: string
    description: string
    status: string
    created_date: Date
    mod_date: Date
    media_ids?: string[]
}
/**
 * To record contributions of Users to Tasks
*/
export interface Contribution {
    user_id: string
    role: string
    result: string
}
/**
 * The highest level activity. Parent_id can point to a parent @interface Project.
*/
export interface Project extends BaseActivity { //to other collection
    owner_id: string
}
/**
 * Activities that have a specific start and end time, and optionally, subtasks.
 * Parent_id can point to a @interface Project.
*/
export interface Action extends BaseActivity {
    start: Date
    end: Date
    location: string
    tasks?: Task[]
}

export interface Task extends BaseActivity {
    deadline: Date
    cost_est?: string
    work_est?: string
    responsible_id?: string
    contribution_ids?: Contribution[]
}
