const EMAIL = 'test@test.se'
const FIRSTNAME = 'test'
const LASTNAME = 'testson'
const BASE = 'http://localhost:5000'

describe('1. R8UC1', () => {
    beforeEach(() => {

        cy.visit('http://localhost:3000');

        // Check if user exists, if true, lets reinitialize it!
        cy.request({
            method: 'GET',
            url: `${BASE}/users/bymail/${EMAIL}`,
            failOnStatusCode: false
        }).then((response) => {
            if (response.status === 200) {
                cy.request({
                    method: 'DELETE',
                    url: `${BASE}/users/${response.body._id.$oid}`
                })
                cy.log(`user: ${response.body.email} has been deleted`)
            }

            cy.request({
                method: 'POST',
                url: `${BASE}/users/create`,
                form: true,
                body: {
                    email: EMAIL,
                    firstName: FIRSTNAME,
                    lastName: LASTNAME
                }
            });
            cy.log(`user: ${response.body.email} has been created`)
        });
        
        // Create a new task for the user
        cy.request({
            method: 'GET',
            url: `${BASE}/users/bymail/${EMAIL}`,
            failOnStatusCode: false
        }).then((response) => {
            cy.request({
                method: 'POST',
                url: `${BASE}/tasks/create`,
                form: true,
                body: {
                    title: 'Test task',
                    description: '*Insert todo here*',
                    userid: response.body._id.$oid,
                    url: '',
                    todos: 'Create a todo',
                },
              });  
        });

       // User login
       cy.get('[id=email]').type(EMAIL);
       cy.get('form').submit();

       // Lastly, enters the detail page of the task
       cy.contains('Test task').click();
       
    })
    it("1.1 The user enters a description of a todo item into an empty input form field.", () => {
        cy.get('div').get('.todo-list').get('li').get('.inline-form').find('input[type=text]').type('A new todo item');
        cy.contains('Add').click();
        cy.wait(800); // Make sure that page has finished reloaded
        cy.get('div').get('.todo-list').get('li').get('.todo-item').last().should('include.text', 'A new todo item');
    })

    it("1.2 If the description is not empty and the user presses “Add”, the system creates a new todo item.", () => {
        cy.contains('Add').click();
    })
})